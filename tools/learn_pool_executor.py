import asyncio
from concurrent.futures import ProcessPoolExecutor
import fitz


def sync_parse_pdf(file_path: str) -> str:
    """纯同步的耗时操作"""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


executor = ProcessPoolExecutor(max_workers=2)


async def parse_pdf_task(file_path: str):
    loop = asyncio.get_running_loop()
    try:
        print(f"开始解析 {file_path}...")
        content = await loop.run_in_executor(executor, sync_parse_pdf, file_path)
        return content
    except Exception as e:
        print(f"解析失败: {e}")
        raise


# 3. 运行示例
async def main():
    start = asyncio.get_event_loop().time()
    result = await asyncio.create_task(
        parse_pdf_task("/Users/mini/Downloads/anthropic文章.pdf")
    )
    end = asyncio.get_event_loop().time()
    print(f"解析完成，总耗时: {end - start:.2f}s")
    if result:
        for l in result.splitlines():
            print(l)


if __name__ == "__main__":
    asyncio.run(main())
