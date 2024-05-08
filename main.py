import os

import flet as ft
from route.routes import router
import pandas as pd


def testxls2xlsx():
    print(os.listdir("/Users/yaosong.zhan/Desktop/excelw/"))
    # 遍历xls文件夹
    for f in os.listdir("/Users/yaosong.zhan/Desktop/excelw/"):
        if f.endswith('.xls'):
            # 获取文件
            xls_file = '/Users/yaosong.zhan/Desktop/excelw/' + f
            # 转换好后的保存文件夹
            xlsx_file = f'/Users/yaosong.zhan/Desktop/excelw/{f.split(".")[0]}.xlsx'

            # 读取xls文件
            xls_data = pd.read_excel(xls_file)

            # 写入xlsx文件
            xls_data.to_excel(xlsx_file, index=False)
            print(f, '转换完成')


def main(page: ft.Page):
    # testxls2xlsx()
    page.on_route_change = router.route_change
    page.window_title_bar_hidden = True
    page.window_width = 800
    page.window_height = 550
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    router.page = page
    page.add(
        router.body
    )
    page.go('/')


ft.app(target=main, assets_dir="assets")
