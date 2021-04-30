module.exports = {
  root: true,
  env: {
    // this section will be used to determine which APIs are available to us
    // (i.e are we running in a browser environment or a node.js env)
    node: true,
    browser: true,
  },
  parserOptions: {
    parser: "babel-eslint",
    // specifying a module sourcetype prevent eslint from marking import statements as errors
    sourceType: "module",
  },
  extends: [
    // use the recommended rule set for both plain javascript and vue
    "eslint:recommended",
    "plugin:vue/recommended",
  ],
  rules: {
    // we should always disable console logs and debugging in production
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-unused-vars": ["error", { "ignoreRestSiblings": true }],
    "max-len": ["error", {
      "code": 140,
      "tabWidth": 2,
      "ignorePattern": "^import.*",
    }],
    "indent": ["error", 2],
    "semi": ["error", "always"],
    "comma-dangle": ["error", {
      "arrays": "always-multiline",
      "objects": "always-multiline",
      "imports": "always-multiline",
      "exports": "always-multiline",
      "functions": "only-multiline",
    }],
    "key-spacing": ["error", { "beforeColon": false }],
    "space-before-function-paren": ["error", "never"],
    "space-infix-ops": "error",
    "keyword-spacing": ["error", { "before": true }],
    "comma-spacing": ["error", { "before": false, "after": true }],
    "no-multiple-empty-lines": ["error", { "max": 1, "maxEOF": 1 }],
    "no-multi-spaces": "error",
  },
};