#!/bin/sh
echo -n 'what is the value?'
read value
sed 's/XYZ/'"$value"'/' <<EOF
The value is XYZ
EOF
