#!/bin/bash
# displays the size of the body of the response

curl -w '%[size_download}\n' -so /dev/null $1
