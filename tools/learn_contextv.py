import asyncio
import contextvars
from typing import NamedTuple


class RequestContext(NamedTuple):
    user_id: str
    trace_id: str
    is_admin: bool = False


ctx_var = contextvars.ContextVar("ctx", default=None)


async def tool_call():
    ctx = ctx_var.get()
    print(f"[Tool]当前 context: {ctx}")
    await asyncio.sleep(0.1)
    return ctx


async def handle_request(user: str, tid: str):
    ctx = RequestContext(user_id=user, trace_id=tid)
    ctx_var.set(ctx)
    r = await tool_call()
    return r


async def handle_request_usb(user: str, tid: str):
    ctx = RequestContext(user_id=user, trace_id=tid)
    ctx_var.set(ctx)
    r = await asyncio.create_task(tool_call())
    return r


async def check_admin(user: str):
    await asyncio.sleep(0.1)
    return True if user == "AAA" else False


async def handle_request_with_update(user: str, tid: str):
    ctx = RequestContext(user_id=user, trace_id=tid)
    ctx_var.set(ctx)
    print(f"初始请求: {ctx}")
    admin = await check_admin(user)
    if admin:
        cur_ctx = ctx_var.get()
        new_ctx = cur_ctx._replace(is_admin=True)
        ctx_var.set(new_ctx)
        print(f"更新请求: {ctx}")
    r = await asyncio.create_task(tool_call())
    return r


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(handle_request("AAA", "TX-101"))
        t2 = tg.create_task(handle_request_usb("BBB", "TX-102"))
        t3 = tg.create_task(handle_request_with_update("AAA", "TX-103"))
        tasks.append(t1)
        tasks.append(t2)
        tasks.append(t3)
    for t in tasks:
        print(f"task-result={t.result()}")


if __name__ == "__main__":
    asyncio.run(main())
