#!/bin/bash
 
 if [ -z "$1" ]; then
     echo "Usage: $0 folder_name"
     exit 1
 fi
 
 mkdir "$1" && cd "$1" || exit
 
 touch index.ts "${1}.tsx" "types.ts" "${1}.styles.ts"
 
 echo "export * from './types'" >> index.ts
 echo "export * from './${1}'" >> index.ts
 echo "export * from './${1}.styles'" >> index.ts
 
 echo "import { ${1}Container } from './${1}.styles';" >> "${1}.tsx"
 echo "import { ${1}Props } from './types';" >> "${1}.tsx"
 echo "" >> "${1}.tsx" # Empty line
 echo "export const ${1} = ({}: ${1}Props) => {" >> "${1}.tsx"
 echo " return <${1}Container></${1}Container>;" >> "${1}.tsx"
 echo "};" >> "${1}.tsx"
 
 echo "export interface ${1}Props {}" >> "types.ts"
 
 echo "import { styled } from '@mui/system';" > "${1}.styles.ts"
 echo "" >> "${1}.styles.ts"
 echo "export const ${1}Container = styled('div')\`\`;" >> "${1}.styles.ts"
