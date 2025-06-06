#!/bin/bash

# Function to convert string to kebab case
to_kebab_case() {
    echo "$1" | sed -E 's/([a-z0-9])([A-Z])/\1-\2/g' | tr '[:upper:]' '[:lower:]'
}

# Parse command line arguments
USE_KEBAB=false
COMPONENT_NAME=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -k|--kebab)
            USE_KEBAB=true
            shift
            ;;
        *)
            COMPONENT_NAME="$1"
            shift
            ;;
    esac
done

if [ -z "$COMPONENT_NAME" ]; then
    echo "Usage: $0 [-k|--kebab] component_name"
    exit 1
fi

# Convert component name to Pascal case for the component itself
PASCAL_CASE=$(echo "$COMPONENT_NAME" | sed -E 's/(^|_|-)([a-z])/\U\2/g')

# Use kebab case for files if flag is set
if [ "$USE_KEBAB" = true ]; then
    FILE_NAME=$(to_kebab_case "$COMPONENT_NAME")
else
    FILE_NAME="$COMPONENT_NAME"
fi

mkdir "$FILE_NAME" && cd "$FILE_NAME" || exit

touch index.ts "${FILE_NAME}.tsx" "types.ts" "${FILE_NAME}.styles.ts"

echo "export * from './types'" >> index.ts
echo "export * from './${FILE_NAME}'" >> index.ts
echo "export * from './${FILE_NAME}.styles'" >> index.ts

echo "import { ${PASCAL_CASE}Container } from './${FILE_NAME}.styles';" >> "${FILE_NAME}.tsx"
echo "import { ${PASCAL_CASE}Props } from './types';" >> "${FILE_NAME}.tsx"
echo "" >> "${FILE_NAME}.tsx"
echo "export const ${PASCAL_CASE} = ({}: ${PASCAL_CASE}Props) => {" >> "${FILE_NAME}.tsx"
echo " return <${PASCAL_CASE}Container></${PASCAL_CASE}Container>;" >> "${FILE_NAME}.tsx"
echo "};" >> "${FILE_NAME}.tsx"

echo "export interface ${PASCAL_CASE}Props {}" >> "types.ts"

echo "import { styled } from '@mui/material';" > "${FILE_NAME}.styles.ts"
echo "" >> "${FILE_NAME}.styles.ts"
echo "export const ${PASCAL_CASE}Container = styled('div')\`\`;" >> "${FILE_NAME}.styles.ts"
