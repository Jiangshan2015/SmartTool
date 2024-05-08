from route.Router import Router, DataStrategyEnum
from views.index_view import IndexView
from views.help import HelpView
from views.read_file import ReadFileView
from views.write_file import WriteFileView
from views.code import CodeView

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    "/": IndexView,
    "/help": HelpView,
    "/read": ReadFileView,
    "/write": WriteFileView,
    "/code": CodeView,
}
