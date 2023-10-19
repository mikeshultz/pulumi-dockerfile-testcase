import pulumi

from pathlib import Path
from pulumi_awsx.ecr import Image, Repository

stack = pulumi.get_stack()

repository = Repository(f"{stack}-repository")
image = Image(
    "pulumi-dockerfile-testcase",
    repository_url=repository.url,
    # Relative
    #dockerfile="Dockerfile.testcase",
    # Absolute
    dockerfile=Path(__file__).parent.joinpath("Dockerfile.testcase").as_posix(),
)

pulumi.export("image_url", image.image_uri)
