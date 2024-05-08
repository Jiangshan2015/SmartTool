import flet as ft


# iconColors = ['0xff0ba360', '0xffa56cc1', '0xffb83b5e', '0xff9896f1', '0xff1e56a0', '0xfff3d7ca']
# startColors = ['0xffa18cd1', '0xffa1c4fd', '0xff6a85b6', '0xfffdfcfb', '0xfff78ca0', '0xff0ba360']
# endColors = ['0xfffbc2eb', '0xffc2e9fb', '0xffbac8e0', '0xffe2d1c3', '0xfffe9a8b', '0xff3cba92']


# 点击事件


def IndexView(page: ft.Page):
    def click_container(index):
        if index == 0:
            return lambda e: e.page.go("/read")
        elif index == 1:
            return lambda e: e.page.go("/write")
        elif index == 2:
            return lambda e: e.page.go("/code")
        elif index == 5:
            return lambda e: e.page.go("/help")
        else:
            return

    def cell_widget(icon, name, index):
        # start_color = startColors[index]
        # end_color = endColors[index]
        return ft.Container(
            image_src=f"../assets/cell_bg_0{index}.jpeg",
            image_fit=ft.ImageFit.COVER,
            content=ft.Column([
                ft.Image(
                    src=f"icon_0{index}.png",
                    width=60,
                    height=60,
                    fit=ft.ImageFit.COVER,
                    repeat=ft.ImageRepeat.NO_REPEAT,
                    border_radius=ft.border_radius.all(30),
                ),
                ft.Text(name, size=17, color='white'),
            ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,

            ),
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            width=225,
            height=145,
            border_radius=10,
            ink=True,
            # gradient=ft.LinearGradient(
            #     begin=ft.alignment.top_center,
            #     end=ft.alignment.bottom_center,
            #     colors=[
            #         start_color, end_color
            #     ],
            #     tile_mode=ft.GradientTileMode.MIRROR,
            # ),
            on_click=click_container(index),
        )

    content = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        alignment=ft.alignment.center,
                        width=220,
                        height=60,
                    ),
                ]
            ),
            ft.Row(
                [
                    cell_widget(ft.icons.MARKUNREAD, "读取文件", 0),
                    cell_widget(ft.icons.PRINT, "写入文件", 1),
                    cell_widget(ft.icons.TRACK_CHANGES, "批量生成码", 2),

                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

            ft.Row(
                [
                    cell_widget(ft.icons.OTHER_HOUSES, "未开发", 3),
                    cell_widget(ft.icons.FIND_REPLACE, "未开发", 4),
                    cell_widget(ft.icons.HELP, "使用帮助", 5),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
    )
    container = ft.Container(
        image_src=f"../assets/bg_image.jpeg",
        image_fit=ft.ImageFit.COVER,
        width=800,
        height=550,
        content=content,
    )
    return content
