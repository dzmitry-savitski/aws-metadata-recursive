# aws-metadata-recursive
A small script to list all AWS metadata recursively. Useful when you have RCE on a target server and want to retrive all metadata.

# Usage:
```
python3 metadata.py
```

# Example output:
```
http://169.254.169.254/latest/meta-data/
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
events/
hibernation/
hostname
iam/
identity-credentials/
instance-action
instance-id
instance-life-cycle
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
reservation-id
security-groups
services/
system
----------------------------------------------------------------------------------------------------
http://169.254.169.254/latest/meta-data/ami-id
ami-0128e8b118981xxxx
----------------------------------------------------------------------------------------------------
http://169.254.169.254/latest/meta-data/ami-launch-index
0
----------------------------------------------------------------------------------------------------
http://169.254.169.254/latest/meta-data/ami-manifest-path
(unknown)
----------------------------------------------------------------------------------------------------
http://169.254.169.254/latest/meta-data/block-device-mapping/
ami
root
----------------------------------------------------------------------------------------------------
http://169.254.169.254/latest/meta-data/block-device-mapping/ami
/dev/sda1
```
