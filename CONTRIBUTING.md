# Contributing to Constable
Hi there! Thanks for taking the time to contribute to our github repo.

The following is a set of guidelines for contributing to our repository which has an implementation of automated code and file review i.e look for the presence of files, correct references, review if releases exist, etc. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

# Code of Conduct
This project and everyone participating in it is governed by our [Code of Conduct](./CODE-OF-CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to ygangwa@ncsu.edu.

# How To Contribute


## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Attach issue id in the commit message for easier tracking

### JavaScript Styleguide

All JavaScript must adhere to [JavaScript Standard Style](https://standardjs.com/).

* Prefer the object spread operator (`{...anotherObj}`) to `Object.assign()`
* Inline `export`s with expressions whenever possible
  ```js
  // Use this:
  export default class ClassName {

  }

  // Instead of:
  class ClassName {

  }
  export default ClassName
  ```
* Place requires in the following order:
    * Built in Node Modules (such as `path`)
    * Built in Atom and Electron Modules (such as `atom`, `remote`)
    * Local Modules (using relative paths)
* Place class properties in the following order:
    * Class methods and properties (methods starting with `static`)
    * Instance methods and properties
* [Avoid platform-dependent code](https://flight-manual.atom.io/hacking-atom/sections/cross-platform-compatibility/)
* All files must end in a new line


### HTML Styleguide

All HTML must adhere to [HTML Standard Style](https://google.github.io/styleguide/htmlcssguide.html).

* Use HTTPS for embedded resources where possible.
* Indent by 2 spaces at a time.
    * Don’t use tabs or mix tabs and spaces for indentation.
* Use only lowercase.
* Remove trailing white spaces.
* Make sure your editor uses UTF-8 as character encoding, without a byte order mark.
* HTML5 (HTML syntax) is preferred for all HTML documents: <!DOCTYPE html>.
* Use valid HTML where possible.
* Provide alternative contents for multimedia.
* Separate structure from presentation from behavior.
* Do not use entity references.
* Use a new line for every block, list, or table element, and indent every such child element.


## Tools

### Testing

Testing is important. We utilize `jest` for our unit tests and continually run tests via GitHub actions for pull requests and pushes directly to main. If you open a pull request, you will need to pass the CI tests in order to merge changes.

### The Kanban Board for Constable.

The [Kanban Board](https://github.com/dangoslen/constable-github-action/projects/1) is used for all issues/feature requests. All items that require any code changes should be converted to issues, tagged with the appropriate milestone, and then progress can be tracked using issues.

### Pull Requests

The process described here has several goals:

- Maintain quality
- Fix problems that are important to users
- Engage the community by creating a contributable environment

Please follow these steps to have your contribution reviewed by the maintainers:

1. Include a clear and descriptive title.
2. Include a description of the change.

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Attribution

The Contributing guidelines above are adapted from [Atom][homepage].

[homepage]: https://github.com/atom/atom
