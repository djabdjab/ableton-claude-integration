#!/usr/bin/env python3
"""
Upload Ableton-Claude guide to Notion page
"""

import json
import requests
import re
import os

NOTION_TOKEN = os.environ.get("NOTION_API_TOKEN")
PAGE_ID = os.environ.get("NOTION_PAGE_ID", "2e3a38e2-a837-807c-95c3-d926807be2a9")
NOTION_VERSION = "2022-06-28"

if not NOTION_TOKEN:
    print("❌ Error: NOTION_API_TOKEN environment variable not set")
    print("Usage: NOTION_API_TOKEN=your_token python3 notion_upload.py")
    exit(1)

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": NOTION_VERSION
}

def text_block(content):
    """Create a paragraph block"""
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {"content": content[:2000]}  # Notion limit
            }]
        }
    }

def heading_1_block(content):
    """Create a heading 1 block"""
    return {
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "rich_text": [{
                "type": "text",
                "text": {"content": content[:2000]}
            }]
        }
    }

def heading_2_block(content):
    """Create a heading 2 block"""
    return {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{
                "type": "text",
                "text": {"content": content[:2000]}
            }]
        }
    }

def heading_3_block(content):
    """Create a heading 3 block"""
    return {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [{
                "type": "text",
                "text": {"content": content[:2000]}
            }]
        }
    }

def code_block(content, language="bash"):
    """Create a code block"""
    return {
        "object": "block",
        "type": "code",
        "code": {
            "rich_text": [{
                "type": "text",
                "text": {"content": content[:2000]}
            }],
            "language": language
        }
    }

def bulleted_list_item(content):
    """Create a bulleted list item"""
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{
                "type": "text",
                "text": {"content": content[:2000]}
            }]
        }
    }

def parse_markdown_to_blocks(markdown_content):
    """Convert markdown to Notion blocks"""
    blocks = []
    lines = markdown_content.split('\n')

    in_code_block = False
    code_content = []
    code_language = "bash"

    i = 0
    while i < len(lines):
        line = lines[i]

        # Handle code blocks
        if line.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_language = line[3:].strip() or "bash"
                code_content = []
            else:
                in_code_block = False
                if code_content:
                    blocks.append(code_block('\n'.join(code_content), code_language))
                code_content = []
            i += 1
            continue

        if in_code_block:
            code_content.append(line)
            i += 1
            continue

        # Handle headings
        if line.startswith('# '):
            blocks.append(heading_1_block(line[2:].strip()))
        elif line.startswith('## '):
            blocks.append(heading_2_block(line[3:].strip()))
        elif line.startswith('### '):
            blocks.append(heading_3_block(line[4:].strip()))
        # Handle bullet points
        elif line.startswith('- ') or line.startswith('* '):
            blocks.append(bulleted_list_item(line[2:].strip()))
        # Handle numbered lists as bullets (Notion will auto-number if needed)
        elif re.match(r'^\d+\.\s', line):
            content = re.sub(r'^\d+\.\s', '', line).strip()
            blocks.append(bulleted_list_item(content))
        # Handle regular text (skip empty lines)
        elif line.strip() and not line.startswith('---'):
            blocks.append(text_block(line.strip()))

        i += 1

    return blocks

def upload_blocks_to_notion(blocks, batch_size=100):
    """Upload blocks to Notion page in batches"""
    url = f"https://api.notion.com/v1/blocks/{PAGE_ID}/children"

    # Notion API has a limit of 100 blocks per request
    for i in range(0, len(blocks), batch_size):
        batch = blocks[i:i+batch_size]
        data = {"children": batch}

        response = requests.patch(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"✅ Uploaded batch {i//batch_size + 1} ({len(batch)} blocks)")
        else:
            print(f"❌ Error uploading batch {i//batch_size + 1}: {response.status_code}")
            print(response.text)
            return False

    return True

def main():
    # Read the markdown guide
    with open('/Users/jabali/ableton-claude-integration/NOTION_GUIDE.md', 'r') as f:
        markdown_content = f.read()

    print("📝 Parsing markdown content...")
    blocks = parse_markdown_to_blocks(markdown_content)
    print(f"✅ Created {len(blocks)} blocks")

    print(f"📤 Uploading to Notion page {PAGE_ID}...")
    success = upload_blocks_to_notion(blocks)

    if success:
        print("✅ Successfully uploaded all content to Notion!")
        print(f"🔗 View at: https://www.notion.so/Ableton-{PAGE_ID}")
    else:
        print("❌ Upload failed")

if __name__ == "__main__":
    main()
