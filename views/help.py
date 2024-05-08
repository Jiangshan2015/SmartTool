from typing import Union
import flet as ft
from route.Router import Router


def HelpView(router: Union[Router, str, None] = None):
    def goback(e: ft.ControlEvent):
        router.page.controls.pop()
        e.page.go("/")

    router.page.add(
        ft.Container(
            margin=ft.margin.only(top=20),
            content=ft.Row(
                [
                    ft.FilledButton("返回首页", icon="ARROW_BACK_IOS_OUTLINED", on_click=goback),
                    ft.Card(
                        width=600,
                        height=450,
                        content=ft.Container(
                            image_src=f"../assets/bg_content_help.jpeg",
                            image_fit=ft.ImageFit.COVER,
                            border_radius=5,
                            padding=10,
                            content=ft.Column(
                                [
                                    ft.Text("1、程序异常崩溃闪退，重启电脑解决"),
                                    ft.Text("2、Excel的格式一定要正确,以.xlsx结尾的"),
                                    ft.Text("3、程序运行时，不要手动打开excel，如打开请关闭"),
                                    ft.Text("4、若拷贝smart_tool_images文件夹到桌面，则可省略读取文件"),
                                    ft.Text("5、桌面生成的smart_tool_images文件夹不要删除"),
                                    ft.Text("6、如果程序一直在进度条动画，有可能报错了"),
                                    ft.Text("7、定期清理电脑垃圾，不行就换"),
                                    ft.Text("8、windows系统上遇到的兼容性问题，等我一万年以后更新"),
                                    ft.Text("9、如商业使用，谨慎使用，造成损失概不负责"),
                                ]
                            )
                        )),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        ),
    )
