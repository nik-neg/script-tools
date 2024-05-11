import os
import re

def to_kebab_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '-', name).lower()

def apply_data_test_ids(content):
    stack = []

    tag_pattern = re.compile(r'<(/?)(\w+)([^>]*?)(/?)>', re.DOTALL)

    def replace_function(match):
        is_closing = match.group(1) == '/'
        tag_name = match.group(2)
        attrs = match.group(3)
        is_self_closing = match.group(4) == '/'

        if is_closing:
            if stack:
                stack.pop()
        else:
            if 'data-testid' not in attrs:
                parent_name = stack[-1] if stack else ''
                test_id = f"{to_kebab_case(parent_name)}-{to_kebab_case(tag_name)}" if parent_name else to_kebab_case(tag_name)
                attrs = attrs.strip() + f' data-testid="{test_id}"'
            if not is_self_closing:
                stack.append(tag_name)
            return f'<{tag_name} {attrs}{" /" if is_self_closing else ""}>'
        return match.group(0)

    # Apply regular test-id insertion to all elements
    jsx_blocks = re.finditer(r'return\s*\(([\s\S]*?)\);', content, re.MULTILINE)
    for block in jsx_blocks:
        start, end = block.span(1)
        jsx_content = block.group(1)
        updated_jsx_content = re.sub(tag_pattern, replace_function, jsx_content)
        content = content[:start] + updated_jsx_content + content[end:]

    return content

def add_data_test_id_to_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.tsx'):
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated_content = apply_data_test_ids(content)

                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

# Path to the 'src' directory of your React project
src_path = '../client/src'
add_data_test_id_to_files(src_path)
