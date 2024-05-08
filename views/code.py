from typing import Union
import flet as ft

from route.Router import Router
from time import sleep
import os
from tool.smart_tool import SmartTool as sl
import barcode
from barcode.writer import ImageWriter
import qrcode


def CodeView(router: Union[Router, str, None] = None):
    pb = ft.ProgressBar(width=400, visible=False)
    dir_pre = "选择的文件："
    directory_path = ft.Text(dir_pre)
    # file_path = ''
    progress_state = ft.Text("")

    # 返回
    def goback(e: ft.ControlEvent):
        close_banner(e)
        router.page.controls.pop()
        e.page.go("/")

    # Open directory dialog
    def pick_files_result(e: ft.FilePickerResultEvent):
        if len(e.files) > 0:
            directory_path.value = dir_pre + e.files[0].path
        directory_path.update()

    def close_banner(e):
        router.page.banner.open = False
        router.page.update()

    router.page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=20),
        content=ft.Text(
            "ooo，选择正确的文件（txt文本）"
        ),
        actions=[
            ft.TextButton(" "),
            ft.TextButton("忽略", on_click=close_banner),
        ],
    )

    def handleQRFiles():
        save_dir = sl.makeDir('Smart_tool_qr')
        file_path = directory_path.value.removeprefix(dir_pre)
        with open(file_path, "r") as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                img = qrcode.make(line)
                # 显示图片格式，为qrcode.image.pil.PilImage
                # 保存图片
                img.save(save_dir + "/" + line + ".png")

    def handleBarFiles():
        save_dir = sl.makeDir('Smart_tool_bar')
        file_path = directory_path.value.removeprefix(dir_pre)
        with (open(file_path, "r") as f):
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                bar = barcode.get('ean13', line, writer=ImageWriter())
                bar.save(save_dir + "/" + line)

    def qr_file(e: ft.FilePickerResultEvent):
        router.page.banner.open = False
        router.page.update()
        if directory_path.value == dir_pre:
            router.page.banner.open = True
            router.page.update()
            return
        pb.visible = True
        handleQRFiles()
        progress_state.value = "正在生成二维码，稍后..."
        router.page.update()
        sleep(1)
        progress_state.value = "二维码生成完成"
        pb.value = 1
        router.page.update()

    def bar_file(e: ft.FilePickerResultEvent):
        router.page.banner.open = False
        router.page.update()
        if directory_path.value == dir_pre:
            router.page.banner.open = True
            router.page.update()
            return
        pb.visible = True
        handleBarFiles()
        progress_state.value = "正在生成条形码，稍后..."
        router.page.update()
        sleep(1)
        progress_state.value = "条形码生成完成"
        pb.value = 1
        router.page.update()

    # get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    router.page.overlay.extend([pick_files_dialog])
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
                            image_src=f"../assets/bg_content.jpeg",
                            image_fit=ft.ImageFit.COVER,
                            border_radius=5,
                            content=ft.Column(
                                [
                                    ft.Container(
                                        ft.Text(
                                            "备注.生成的条形码、二维码分别在桌面Smart_tool_bar、Smart_tool_qr文件夹中。条形码只能是数字并且大于12位",
                                            size=14,
                                            max_lines=3
                                        ),
                                        width=600,
                                        height=60,
                                        padding=10
                                    ),
                                    ft.Container(
                                        width=600,
                                        height=50,
                                        alignment=ft.alignment.center,
                                        content=ft.FilledButton(
                                            "打开文件",
                                            icon=ft.icons.FILE_COPY_ROUNDED,
                                            on_click=lambda _: pick_files_dialog.pick_files(
                                                allow_multiple=True
                                            ),
                                        ),
                                    ),
                                    # ft.icons.UPLOAD
                                    ft.Container(
                                        width=600,
                                        height=70,
                                        padding=10,
                                        alignment=ft.alignment.center,
                                        content=directory_path,
                                    ),
                                    ft.FilledButton("生成条形码", icon="QR_CODE_2", on_click=bar_file),
                                    ft.FilledButton("生成二维码", icon="QR_CODE", on_click=qr_file),
                                    ft.Container(
                                        width=600,
                                        height=50,
                                        alignment=ft.alignment.center,
                                        content=ft.Column([progress_state, pb]),
                                    ),

                                ],
                                wrap=True,
                                spacing=30,
                                run_spacing=10,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        )),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.START
            )
        ),
    )
