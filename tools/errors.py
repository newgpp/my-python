from typing import Any


class DomainError(Exception):
    """所有业务域异常的基类"""

    # * 用来规定：它后面的参数只能用“参数名”传递，不能用位置传参
    def __init__(self, message: str, *, details: dict[str, Any] | None = None):
        super().__init__(message)
        self.details = details or {}


class ValidationError(DomainError):
    """输入校验失败"""


class NotFoundError(DomainError):
    """资源不存在"""


class ExternalServiceError(DomainError):
    """第三方服务异常"""
