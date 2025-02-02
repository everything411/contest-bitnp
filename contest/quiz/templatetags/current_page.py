"""检测当前页面

需要`constants.ROUTES`。
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from django import template
from django.urls import Resolver404, resolve

if TYPE_CHECKING:
    from http import HTTPStatus

    from django.http import HttpRequest

    from quiz.constants import ConstantsNamespace


register = template.Library()


@register.simple_tag(takes_context=True)
def current_page_title(context: dict, default: str = "") -> str:
    """当前页面的标题

    1. 查找`constants.ROUTES: dict[str, PageMeta]`。
    2. 若无匹配，则尝试`response_status: HTTPStatus`。
    3. 若也无，则返回`default`。
    """
    request: HttpRequest = context["request"]
    if "constants" in context:
        constants: ConstantsNamespace = context["constants"]
        try:
            view_name = resolve(request.path_info).view_name
        except Resolver404:
            pass
        else:
            if view_name in constants.ROUTES:
                page = constants.ROUTES[view_name]
                return page.title

    if "response_status" in context:
        status: HTTPStatus = context["response_status"]
        return f"{status.value} {status.phrase}"

    return default
