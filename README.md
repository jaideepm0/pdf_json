Documentation:

The build commands to use the `code`

BUILD:
```
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

TEST RUN:
```
docker run --rm \    
  -v "$(pwd)/test/input:/app/input" \
  -v "$(pwd)/test/output:/app/output" \
  --network none \
  mysolutionname:somerandomidentifier
```

Due no Internet access `python` is used to rather than `uv`
- uses `pymupdf4llm` to parse the `pdf` to `md`
- uses the `md` heading structure to `extract` the headings from the pages
- vanilla builtin `json` package is used to generate the `.json` output files
- vanilla builtin `pathlib` handles the file path for read/write operations

Final Notes:
- For general use purposes build and run the docker container based on provided commands
- `input` && `output` directories are for just for testing purpose
