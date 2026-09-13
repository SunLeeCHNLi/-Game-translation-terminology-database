// Extracts the multi-language story / section titles that the Blue Archive story
// viewer keeps as TypeScript array literals.
//
// Usage:  node extract_ts_titles.mjs
// Env:    BA_INPUT_DIR  root folder holding the cloned source repos
//                      (default: E:\Download\BT\Codex_input)
//
// Output: ts_titles.json next to this script.
import fs from "node:fs";
import path from "node:path";
import url from "node:url";

const here = path.dirname(url.fileURLToPath(import.meta.url));
const input = process.env.BA_INPUT_DIR || "E:\\Download\\BT\\Codex_input";
const srcDir = path.join(
  input,
  "ba-archive-blue-archive/apps/blue-archive-story-viewer/src/index",
);

function sliceBalanced(text, openIndex) {
  let depth = 0;
  let inStr = null;
  for (let i = openIndex; i < text.length; i += 1) {
    const c = text[i];
    if (inStr) {
      if (c === "\\") i += 1;
      else if (c === inStr) inStr = null;
      continue;
    }
    if (c === '"' || c === "'" || c === "`") inStr = c;
    else if (c === "[" || c === "{") depth += 1;
    else if (c === "]" || c === "}") {
      depth -= 1;
      if (depth === 0) return text.slice(openIndex, i + 1);
    }
  }
  throw new Error("unbalanced literal");
}

function grab(text, declMarker) {
  const at = text.indexOf(declMarker);
  if (at < 0) throw new Error(`not found: ${declMarker}`);
  const open = text.indexOf("[", text.indexOf("=", at));
  // eslint-disable-next-line no-new-func
  return new Function(`"use strict"; return (${sliceBalanced(text, open)});`)();
}

const read = (f) => fs.readFileSync(path.join(srcDir, f), "utf8");

const out = {
  main: grab(read("mainStoryIndex.ts"), "export const stories"),
  event: grab(read("eventStoryIndex.ts"), "export const stories"),
  eventPlaces: grab(read("eventStoryIndex.ts"), "export const placeMap"),
  other: grab(read("otherStoryIndex.ts"), "export const stories"),
};

for (const [k, v] of Object.entries(out)) {
  console.log(`${k}: ${Array.isArray(v) ? v.length : "?"}`);
}

fs.writeFileSync(path.join(here, "ts_titles.json"), JSON.stringify(out));
console.log("wrote ts_titles.json");
