!# /bin/bash

echo "what's your name?"

read name

if [ "$name" = "john" ]; then

echo "Welcome $name! Here is the secret: Your_Script"

else

echo "Sorry $name! you are not authorized to access"
fi
