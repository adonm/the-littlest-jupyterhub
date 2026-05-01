(requirements)=

# Server Requirements

(supported-os)=

## Operating System

The Littlest JupyterHub (TLJH) aims to support Debian and Ubuntu versions that have current Long-Term Support (LTS), on amd64 or arm64 CPU architectures.
Other Linux distributions are not supported.

## Root access

Full `root` access to this server is required. This might be via `sudo`
(recommended) or by direct access to `root` (not recommended!)

## External IP

An external IP allows users on the internet to reach your JupyterHub. Most
VPS / Cloud providers give you a public IP address along with your server. If
you are hosting on a physical machine somewhere, talk to your system administrators
about how to get HTTP traffic from the world into your server.

## CPU / Memory / Disk Space

See how to [](/howto/admin/resource-estimation)
