# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.1] - 2025-07-03

### Added
- Initial release of rankedpairsvoting package
- Core `ranked_pairs_voting()` function
- `TotalOrderGraph` class for maintaining and establishing candidate ordering
- Support for any number of candidates and voters
- Fair tie resolution through randomization
- Basic documentation and usage examples

## [0.0.2] - 2025-07-09

### Fixed
- Refactored `TotalOrderGraph` to `PartialOrderGraph` for correct handling of candidate ordering

### Added
- Improved documentation and usage examples
- Included more comprehensive test cases

[Unreleased]: https://github.com/hakai-vulpes/ranked-pairs-voting/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/hakai-vulpese/ranked-pairs-voting/releases/tag/v0.0.1
[0.0.2]: https://github.com/hakai-vulpese/ranked-pairs-voting/compare/v0.0.1...v0.0.2