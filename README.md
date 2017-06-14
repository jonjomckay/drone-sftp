# drone-sftp
[![drone-sftp on Docker Hub](https://img.shields.io/docker/automated/jonjomckay/drone-sftp.svg)](https://hub.docker.com/r/jonjomckay/drone-sftp/)

This is a Python [Drone](https://github.com/drone/drone) plugin to sync files to remote hosts using SFTP, based on the features of the [drone-rsync](https://github.com/Drillster/drone-rsync) plugin.

## Usage

### Config
The following parameters are used to configure the plugin:
- **user** - user to log in as on the remote machines
- **key** - private SSH key for the remote machines
- **host** - hostname or IP address of the remote machine
- **port** - port to connect to on the remote machine (defaults to `22`)
- **source** - source folder to synchronize from
- **target** - target folder on the remote machine to synchronize to
- **include** - include filter
- **exclude** - exclude filter

It is highly recommended to put your **key** into a secret so it is not exposed to users. This can be done using the drone-cli:

```sh
drone secret add octocat/hello-world SFTP_KEY @path/to/.ssh/id_rsa
```

Add the secret to your `.drone.yml`:

```yaml
pipeline:
  sftp:
    image: jonjomckay/drone-sftp
    user: some-user
    key: ${SFTP_KEY}
    secrets: [SFTP_KEY]
    host: example.com
    source: ./dist
    target: ~/packages
    exclude: ['^.git/', '.drone.yml']
```

## Building
Build the docker image by running:

```bash
docker build --rm=true -t jonjomckay/drone-sftp .
```
