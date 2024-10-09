# Codebase Conventions

This are guidelines to follow in making this project. This can act as your reference for style-related comments in code reviews.

> This document is yet to expand.

## CSS

### 1. BEM

#### 1.1. Custom CSS should be written in [BEM-syntax](https://getbem.com/introduction/) (block, element, modifier).

- Block
    - Standalone entity with meaning on its own.
    - `header`, `container`, `menu`, `checkbox`, `input`
- Element 
    - A part of a block that has no standalone meaning and is semantically tied to its block.
    - `menu item`, `list item`, `checkbox caption`, `header title`
- Modifier
    - A flag on a block or element. Use them to change appearance or behavior.
    - `disabled`, `highlighted`, `checked`, `color yellow`

The syntax are as follows:

```css
/* Note the indentation on related styles */
.person { }
/* ^^^ -- Block */
    .person__head { }
           /* ^^ -- Element */
    .person--tall { }
           /* ^^ -- Modifier */
    .person__eye--color-blue { }
```

Space separated text are written in kebab-case (whitespace is replaced with one dash `-`).

Elements are appended to blocks with two underscores `__`, and modifiers are appended with two dashes `--`.

#### 1.2. Related styles are indented to emphasize the relation.

#### 1.3. Use the least number of selectors required to style an element.

As a rule, if a selector will work without it being nested then do not nest it.

This is so we only rely on the cascading nature of stylesheets for priority. As CSS prioritizes high specificity in selectors, we can lessen that by using the least amount of selectors and relying on the naming convention instead.

#### 1.4. Only use `!important` proactively.

```css
.one-half {
  width: 50% !important;
}

.hidden {
  display: none !important;
}
```

These two helper, or utility, classes are very specific in their intentions: you would only use them if you wanted something to be rendered at 50% width or not rendered at all. If you didn’t want this behaviour, you would not use these classes, therefore whenever you do use them you will definitely want them to win.

Here we proactively apply `!important` to ensure that these styles always win. This is correct use of !important to guarantee that these trumps always work, and don’t accidentally get overridden by something else more specific.

> DO NOT use `!important` to do hacky CSS overrides.

#### 1.5. Do not use IDs for styling. Use classes instead.

We will use ids for Javascript hooks.

## Git

### 1. Do not directly commit to `main` or `staging` branch.

#### 1.1 Create a development branch, and then pull-request it to `staging`.

Naming convention for branches is:

```
1-feat/pastries-page
^ ------------------------ issue number (optional)
   ^^ -------------------- branch type
       ^^ ---------------- name of branch

```

### 2. Commit names should follow [*conventional commits*](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) format.

Commit message: 
```
<type>(<optional scope>): <description>

<optional body>

<optional footer>
```

Types:
- `feat`: add or remove new features
- `fix`: bug fixes
- `refactor`: restructures code but does not change expected behavior.
- `style`: restructures code to follow style guide
- `test`: add or edit tests
- `doc`: add or edit documentation
- `build`: add, remove, or edit dependencies, version, and other build components
- `chore`: miscellaneous commits e.g. modifying `.gitignore`

Example:
```bash
git commit -m "feat: carousel"
git commit -m "style(navbar): rename classes"
git commit -m "refactor: improve recursion base cases"
```

### 3. Prefer rebase when possible.

### 4. Do not self-merge pull requests.

Request for code review from another collaborator to merge your PR.

### 5. Do not nitpick in code reviews.

Refer only to style guidelines written in this document.

## Typescript

### 1. Prefer arrow syntax for functions and callbacks

```ts
// USE:
const add = (a, b) => a + b

// DO NOT USE:
function add(a, b) {
    return a + b
}
```

### 2. Use absolute paths when it comes to imports.
