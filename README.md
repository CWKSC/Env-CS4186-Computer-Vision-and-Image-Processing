# Note-CS4186-Computer-Vision-and-Image-Processing

Provided Docker image as environment, Windows

Start Docker Desktop first

```
build.cmd
go.cmd
```

After it, you should get into bash shell

```shell
root@env_python_cs4186:/workspace# 
```

## Command for easy use

### Build image

```
build.cmd
```

### Up Container

```
up.cmd
```

### Get into bash shell

```
bash.cmd
```

### Mix up and bash

```
go.cmd
```

### Remove Container

```
down.cmd
```

### Stop Container

```
stop.cmd
```

## Add another python package

Modify `build_venv.cmd`, add `pip3 install <package>`

Remove `venv/` if already exists, Run `build_venv.cmd` to rebuild venv

`requirement.txt` will generated in `resource/`

Run `build.cmd` to rebuild image

