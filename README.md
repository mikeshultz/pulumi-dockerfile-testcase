# Dockerfile issue testcase

Issue showing that `dockerfile` arg on `Image` has no effect.

To run:

```bash
pulumi up -s dev
```

Output:

```
Diagnostics:
  docker:index:Image (image):
    error: could not open dockerfile at relative path Dockerfile: stat Dockerfile: no such file or directory

  pulumi:pulumi:Stack (pulumi-dockerfile-testcase-dev):
    error: Resource monitor has terminated, shutting down
```
