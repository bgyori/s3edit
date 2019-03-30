# S3edit

s3edit allows you to edit files from AWS S3 directly from your terminal.

## Installation

```bash
pip install s3edit
```

## Usage

Assuming your file is at `s3://my-bucket/path/to/file.json`:

```bash
s3edit my-bucket/path/to/file.json
```

## Editor
s3edit uses your `EDITOR` environmental variable to choose an editor. If not
set, `vi` is used by default.

## AWS
Your AWS profile, credentials, and region needs to be set up for s3edit to
work. This can be done through enviromental variables or configuration files.
For more information, see
https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html.
