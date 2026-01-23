# service.py
import httpx
from tools.errors import ExternalServiceError, ValidationError


def fetch_user_balance(user_id: int) -> float:
    """
    异常处理原则（工程约定）：
    1. 只在边界层（IO / 网络 / 接口）做 try/except
    2. 优先捕获具体异常，避免 except Exception
    3. 捕获后必须有“价值动作”：
       - 加上下文（add_note / 日志）
       - 转业务异常（raise BizError(...) from e）
       - 重试 / 降级 / 兜底 / 回滚 / 清理资源
    4. 不静默吞异常（除非明确可忽略且有日志/指标）
    5. broad except 只允许出现在顶层（middleware / CLI main）
    """
    try:
        r = httpx.get(f"https://api.example.com/balance/{user_id}", timeout=6)
        r.raise_for_status()
        return r.json()["balance"]
    except httpx.TimeoutException as e:
        e.add_note(f"user_id={user_id} timeout calling balance api")
        raise ExternalServiceError("外部服务超时") from e
    except httpx.HTTPError as e:
        e.add_note(f"user_id={user_id} http error calling balance api")
        raise ExternalServiceError("外部服务不可用") from e


if __name__ == "__main__":
    fetch_user_balance(12)