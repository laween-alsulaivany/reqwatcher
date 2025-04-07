# ReqWatcher

**Automatically track and record your `pip install` commands in real-time.**

ReqWatcher helps you keep your `requirements.txt` or any other dependency file up to date without the need to remember or manually run `pip freeze`.

---

## Installation

Install locally from source:

```
pip install -e .
```

Once installed, use it via the CLI:

```
reqwatcher install requests flask
```

---

## Features

- **Smart Dependency Tracking**: Automatically appends installed packages to a requirements file.
- **Custom Config Support**: Easily configurable via `.reqwatcher.json`.
- **Undo Last Install**: Roll back the last added dependency.
- **List Tracked Packages**: Show current tracked dependencies.
- **Multiple File Support**: Log to `requirements.txt`, `requirements-dev.txt`, or any custom file.

---

## Usage

### Basic Install & Track

```
reqwatcher install numpy pandas
```

### Undo Last Added Package

```
reqwatcher undo
```

### List All Tracked Packages

```
reqwatcher list
```

---

## Optional Configuration

Create a `.reqwatcher.json` in your project root to customize behavior:

```
{
  "version_format": ">=",
  "auto_add": true,
  "requirement_file": "requirements-dev.txt"
}
```

**Options:**

- `version_format`: `"=="`, `">="`, or `""`
- `auto_add`: Automatically append the package line
- `requirement_file`: The target file to update

If the file is missing or invalid, defaults will be used:

```
{
  "version_format": "==",
  "auto_add": true,
  "requirement_file": "requirements.txt"
}
```

---

## Why Use ReqWatcher?

- No more forgetting to update your requirements file
- Avoid broken production deployments
- Focus on building, not on bookkeeping

---

## Roadmap

- Detect and ignore transitive/indirect dependencies
- Pip plugin hook integration
- Project-level lockfile support
- Docker / Poetry sync commands
- GUI & VS Code integration (eventually)

---

## License

MIT License

---

## Contributing

Have an idea, bug fix, or feature request? Open a PR or file an issue, all contributions are welcome!
