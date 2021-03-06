#!/usr/bin/env python
# coding=utf-8

import os
import json
import uuid
import random
import datetime
import warnings

from pprint import pprint
from pyecharts.option import get_all_options
from pyecharts import template


NBEXT_NAME = 'nbextensions'
DEFAULT_HOST = '/%s' % NBEXT_NAME


class Base(object):

    def __init__(self, title, subtitle,
                 width=800,
                 height=400,
                 title_pos="auto",
                 title_top="auto",
                 title_color="#000",
                 subtitle_color="#aaa",
                 title_text_size=18,
                 subtitle_text_size=12,
                 background_color="#fff"):
        """

        :param title:
            The main title text, supporting for \n for newlines.
        :param subtitle:
            Subtitle text, supporting for \n for newlines.
        :param width:
            Canvas width
        :param height:
            Canvas height
        :param title_pos:
            Distance between grid component and the left side of the container.
            title_pos value can be instant pixel value like 20;
            it can also be percentage value relative to container width like '20%';
            it can also be 'left', 'center', or 'right'.
            If the title_pos value is set to be 'left', 'center', or 'right',
            then the component will be aligned automatically based on position.
        :param title_top:
            Distance between grid component and the top side of the container.
            top value can be instant pixel value like 20;
            it can also be percentage value relative to container width like '20%';
            it can also be 'top', 'middle', or 'bottom'.
            If the left value is set to be 'top', 'middle', or 'bottom',
            then the component will be aligned automatically based on position.
        :param title_color:
            main title text color.
        :param subtitle_color:
            subtitle text color.
        :param title_text_size:
            main title font size
        :param subtitle_text_size:
            subtitle font size
        :param background_color:
            Background color of title, which is transparent by default.
            Color can be represented in RGB, for example 'rgb(128, 128, 128)'.
            RGBA can be used when you need alpha channel, for example 'rgba(128, 128, 128, 0.5)'.
            You may also use hexadecimal format, for example '#ccc'.
        """
        self._option = {}
        self._width, self._height = width, height
        self._colorlst = ['#c23531', '#2f4554', '#61a0a8', '#d48265', '#749f83',
                          '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3',
                          '#f05b72', '#ef5b9c', '#f47920', '#905a3d', '#fab27b',
                          '#2a5caa', '#444693', '#726930', '#b2d235', '#6d8346',
                          '#ac6767', '#1d953f', '#6950a1', '#918597', '#f6f5ec']
        self._option.update(
            title=[{
                "text": title,
                "subtext": subtitle,
                "left": title_pos,
                "top": title_top,
                "textStyle": {"color": title_color, "fontSize": title_text_size},
                "subtextStyle": {"color": subtitle_color, "fontSize": subtitle_text_size}
            }],
            toolbox={
                "show": True,
                "orient": "vertical",
                "left": "right",
                "top": "center",
                "feature": {"saveAsImage": {"show": True}}
            },
            _index_flag=random.randint(1, 9000000),
            tooltip={},
            series=[],
            legend=[{"data": []}],
            backgroundColor=background_color
        )
        self._jshost = DEFAULT_HOST

    def add(self, angle_data=None,
            angle_range=None,
            area_color=None,
            area_opacity=None,
            axis_range=None,
            border_color=None,
            boundary_gap=None,
            center=None,
            clockwise=None,
            datazoom_type=None,
            datazoom_range=None,
            datazoom_orient=None,
            edge_length=None,
            effect_brushtype=None,
            effect_period=None,
            effect_scale=None,
            formatter=None,
            geo_emphasis_color=None,
            geo_normal_color=None,
            grid_width=None,
            grid_height=None,
            grid_top=None,
            grid_bottom=None,
            grid_left=None,
            grid_right=None,
            grid3D_width=None,
            grid3D_height=None,
            grid3D_depth=None,
            grid3D_opacity=None,
            grid3D_shading=None,
            grid3D_rotate_speed=None,
            grid3D_rotate_sensitivity=None,
            gravity=None,
            is_angleaxis_show=None,
            is_area_show=None,
            is_axisline_show=None,
            is_calculable=None,
            is_convert=None,
            is_datazoom_show=None,
            is_emphasis=None,
            is_fill=None,
            is_focusnode=None,
            is_grid3D_rotate=None,
            is_label_show=None,
            is_legend_show=None,
            is_liquid_animation=None,
            is_liquid_outline_show=None,
            is_radiusaxis_show=None,
            is_random=None,
            is_roam=None,
            is_rotatelabel=None,
            is_smooth=None,
            is_splitline_show=None,
            is_stack=None,
            is_step=None,
            is_symbol_show=None,
            is_visualmap=None,
            is_xaxislabel_align=None,
            is_yaxislabel_align=None,
            item_color=None,
            label_color=None,
            label_pos=None,
            label_text_color=None,
            label_text_size=None,
            layout=None,
            legend_orient=None,
            legend_pos=None,
            legend_top=None,
            legend_selectedmode=None,
            line_curve=None,
            line_opacity=None,
            line_type=None,
            line_width=None,
            liquid_color=None,
            maptype=None,
            mark_line=None,
            mark_point=None,
            mark_point_symbol=None,
            mark_point_symbolsize=None,
            mark_point_textcolor=None,
            rader_text_color=None,
            radius_data=None,
            radius=None,
            repulsion=None,
            rosetype=None,
            rotate_step=None,
            scale_range=None,
            shape=None,
            start_angle=None,
            symbol_size=None,
            symbol=None,
            type=None,
            visual_orient=None,
            visual_range_color=None,
            visual_range_size=None,
            visual_range_text=None,
            visual_range=None,
            visual_text_color=None,
            visual_pos=None,
            visual_top=None,
            visual_type=None,
            word_gap=None,
            word_size_range=None,
            x_axis=None,
            xaxis_margin=None,
            xaxis_interval=None,
            xaxis_name_gap=None,
            xaxis_name_size=None,
            xaxis_name_pos=None,
            xaxis_name=None,
            xaxis_rotate=None,
            xaxis_min=None,
            xaxis_max=None,
            xaxis_type=None,
            xaxis3d_name=None,
            xaxis3d_name_size=None,
            xaxis3d_name_gap=None,
            xaxis3d_min=None,
            xaxis3d_max=None,
            xaxis3d_interval=None,
            xaxis3d_margin=None,
            yaxis_margin=None,
            yaxis_interval=None,
            yaxis_formatter=None,
            yaxis_rotate=None,
            yaxis_min=None,
            yaxis_max=None,
            yaxis_name_gap=None,
            yaxis_name_size=None,
            yaxis_name_pos=None,
            yaxis_type=None,
            yaxis_name=None,
            yaxis3d_name=None,
            yaxis3d_name_size=None,
            yaxis3d_name_gap=None,
            yaxis3d_min=None,
            yaxis3d_max=None,
            yaxis3d_interval=None,
            yaxis3d_margin=None,
            zaxis3d_name=None,
            zaxis3d_name_size=None,
            zaxis3d_name_gap=None,
            zaxis3d_min=None,
            zaxis3d_max=None,
            zaxis3d_margin=None):
        """ The base class's add() is just to provide a hint option """
        pass

    def show_config(self):
        """ Print all options of charts"""
        pprint(self._option)

    @staticmethod
    def cast(seq):
        """ Convert the sequence with the dictionary and tuple type into k_lst, v_lst.
        1.[(A1, B1),(A2, B2),(A3, B3),(A4, B4)] --> k_lst[A[i1,i2...]], v_lst[B[i1,i2...]]
        2.[{A1: B1},{A2: B2},{A3: B3},{A4: B4}] --> k_lst[A[i1,i2...]], v_lst[B[i1,i2...]]
        3.{A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[A[i1,i2...]], v_lst[B[i1,i2...]]

        :param seq:
            data sequence
        :return:
        """
        k_lst, v_lst = [], []
        if isinstance(seq, list):
            for s in seq:
                try:
                    if isinstance(s, tuple):
                        _attr, _value = s
                        k_lst.append(_attr)
                        v_lst.append(_value)
                    elif isinstance(s, dict):
                        for k, v in s.items():
                            k_lst.append(k)
                            v_lst.append(v)
                except:
                    raise
        elif isinstance(seq, dict):
            for k, v in seq.items():
                k_lst.append(k)
                v_lst.append(v)
        return k_lst, v_lst

    def _legend_visualmap_colorlst(self, is_visualmap=False, **kwargs):
        """ config legend，visualmap and colorlst component.

        :param is_visualmap:
            It specifies whether to use the viusalmap component.
        :param kwargs:
        """
        kwargs.update(colorlst=self._colorlst)
        chart = get_all_options(**kwargs)
        if is_visualmap:
            self._option.update(visualMap=chart['visual_map'])
        self._option.get('legend')[0].update(chart['legend'])
        self._option.update(color=chart['color'])

        # datazoom component
        if kwargs.get('is_datazoom_show', None) is True:
            self._option.update(dataZoom=chart['datazoom'])

    def render_embed(self):
        """
        Render the chart component and its options

        You can include it into your web pages. And you will
        provide all dependent echarts javascript libraries.
        """
        embed = 'chart_component.html'
        tmp = template.JINJA2_ENV.get_template(embed)
        my_option = json_dumps(self._option, indent=4)
        html = tmp.render(myOption=my_option,
                          chart_id=uuid.uuid4().hex,
                          myWidth=self._width, myHeight=self._height)
        return html

    def render(self, path="render.html"):
        """ Render the options dict, generate the html file

        :param path:
            path of render html file
        """
        _tmp = "local.html"
        my_option = json_dumps(self._option, indent=4)
        tmp = template.JINJA2_ENV.get_template(_tmp)
        html = tmp.render(myOption=my_option,
                          chart_id=uuid.uuid4().hex,
                          myWidth=self._width, myHeight=self._height)
        html = template.freeze_js(html)
        template.write_utf8_html_file(path, html)

    def _repr_html_(self):
        """ Render the options dict, displayed in the jupyter notebook

        :return:
        """
        install_echarts_if_needed()
        divid = datetime.datetime.now()
        my_option = json_dumps(self._option, indent=4)
        _tmp = 'notebook.html'
        series = self._option.get("series")
        map_keywords = {}
        for s in series:
            # Avoid loading too many maps at once, make sure notebook can
            # show map chart normally.
            if s.get('type') == 'map':
                _tmp = "notebook_map.html"
                city_name_in_pinyin = template.CITY_NAME_PINYIN_MAP.get(
                    self._option.get('series')[0].get('mapType'))
                map_keywords['location'] = city_name_in_pinyin
                break
        tmp = template.JINJA2_ENV.get_template(_tmp)
        try:
            html = tmp.render(
                myOption=my_option, chartId=divid, myWidth=self._width,
                myHeight=self._height, host=self._jshost, **map_keywords)
        except:
            html = tmp.render(
                mtOption=my_option.decode('utf8'), chartId=divid,
                myWidth=self._width, myHeight=self._height, host=self._jshost,
                **map_keywords)
        return html

    def render_notebook(self):
        """ Render the options dict, displayed in the jupyter notebook

        :return:
        """
        warnings.warn("\n" + "This function is deprecated since 0.1.9.1" +
                      " Simply passing the chart instance is enough")
        from IPython.display import HTML
        return HTML(self._repr_html_())

    @property
    def _geo_cities(self):
        """ Return China's major cities latitude and longitude -> Geo Chart """
        return {
            '阿城': [126.58, 45.32],
            '阿克苏': [80.19, 41.09],
            '阿勒泰': [88.12, 47.50],
            '阿图什': [76.08, 39.42],
            '安达': [125.18, 46.24],
            '安国': [115.20, 38.24],
            '安康': [109.01, 32.41],
            '安陆': [113.41, 31.15],
            '安庆': [117.02, 30.31],
            '安丘': [119.12, 36.25],
            '安顺': [105.55, 26.14],
            '安阳': [114.35, 36.1],
            '鞍山': [122.85, 41.12],
            '澳门': [115.07, 21.33],
            '巴中': [106.43, 31.51],
            '霸州': [116.24, 39.06],
            '白城': [122.50, 45.38],
            '白山': [126.26, 41.56],
            '白银': [104.12, 36.33],
            '百色': [106.36, 23.54],
            '蚌埠': [117.21, 32.56],
            '包头': [110, 40.58],
            '宝鸡': [107.15, 34.38],
            '保定': [115.48, 38.85],
            '保山': [99.10, 25.08],
            '北海': [109.12, 21.49],
            '北京': [116.46, 39.92],
            '北流': [110.21, 22.42],
            '北票': [120.47, 41.48],
            '本溪': [123.73, 41.3],
            '毕节': [105.18, 27.18],
            '滨州': [118.03, 37.36],
            '亳州': [115.47, 33.52],
            '博乐': [82.08, 44.57],
            '沧州': [116.83, 38.33],
            '昌吉': [87.18, 44.02],
            '昌邑': [119.24, 39.52],
            '常德': [111.69, 29.05],
            '常熟': [120.74, 31.64],
            '常州': [119.95, 31.79],
            '巢湖': [117.52, 31.36],
            '朝阳': [120.27, 41.34],
            '潮阳': [116.36, 23.16],
            '潮州': [116.63, 23.68],
            '郴州': [113.02, 25.46],
            '成都': [104.06, 30.67],
            '承德': [117.93, 40.97],
            '澄海': [116.46, 23.28],
            '赤峰': [118.87, 42.28],
            '赤水': [105.42, 28.34],
            '重庆': [106.54, 29.59],
            '崇州': [103.40, 30.39],
            '滁州': [118.18, 32.18],
            '楚雄': [101.32, 25.01],
            '慈溪': [121.15, 30.11],
            '从化': [113.33, 23.33],
            '达川': [107.29, 31.14],
            '大安': [124.18, 45.30],
            '大理': [100.13, 25.34],
            '大连': [121.62, 38.92],
            '大庆': [125.03, 46.58],
            '大石桥': [122.31, 40.37],
            '大同': [113.3, 40.12],
            '大冶': [114.58, 30.06],
            '丹东': [124.37, 40.13],
            '丹江口': [108.30, 32.33],
            '丹阳': [119.32, 32.00],
            '儋州': [109.34, 19.31],
            '当阳': [111.47, 30.50],
            '德惠': [125.42, 44.32],
            '德令哈': [97.23, 37.22],
            '德兴': [117.35, 28.57],
            '德阳': [104.37, 31.13],
            '德州': [116.29, 37.45],
            '登封': [113.02, 34.27],
            '邓州': [112.05, 32.42],
            '定州': [115.00, 38.30],
            '东川': [103.12, 26.06],
            '东港': [124.08, 39.53],
            '东莞': [113.75, 23.04],
            '东胜': [109.59, 39.48],
            '东台': [120.19, 32.51],
            '东阳': [120.14, 29.16],
            '东营': [118.49, 37.46],
            '都江堰': [103.37, 31.01],
            '都匀': [107.31, 26.15],
            '敦化': [128.13, 43.22],
            '敦煌': [94.41, 40.08],
            '峨眉山': [103.29, 29.36],
            '额尔古纳': [120.11, 50.13],
            '鄂尔多斯': [109.781327, 39.608266],
            '鄂州': [114.52, 30.23],
            '恩平': [112.19, 22.12],
            '恩施': [109.29, 30.16],
            '二连浩特': [111.58, 43.38],
            '番禺': [113.22, 22.57],
            '防城港': [108.20, 21.37],
            '肥城': [116.46, 36.14],
            '丰城': [115.48, 28.12],
            '丰南': [118.06, 39.34],
            '丰镇': [113.09, 40.27],
            '凤城': [124.02, 40.28],
            '奉化': [121.24, 29.39],
            '佛山': [113.11, 23.05],
            '涪陵': [107.22, 29.42],
            '福安': [119.39, 27.06],
            '福清': [119.23, 25.42],
            '福州': [119.3, 26.08],
            '抚顺': [123.97, 41.97],
            '阜康': [87.58, 44.09],
            '阜新': [121.39, 42.01],
            '阜阳': [115.48, 32.54],
            '富锦': [132.02, 47.15],
            '富阳': [119.95, 30.07],
            '盖州': [122.21, 40.24],
            '赣州': [114.56, 28.52],
            '高安': [115.22, 28.25],
            '高碑店': [115.51, 39.20],
            '高密': [119.44, 36.22],
            '高明': [112.50, 22.53],
            '高平': [112.55, 35.48],
            '高要': [112.26, 23.02],
            '高邮': [119.27, 32.47],
            '高州': [110.50, 21.54],
            '格尔木': [94.55, 36.26],
            '个旧': [103.09, 23.21],
            '根河': [121.29, 50.48],
            '公主岭': [124.49, 43.31],
            '巩义': [112.58, 34.46],
            '古交': [112.09, 37.54],
            '广汉': [104.15, 30.58],
            '广水': [113.48, 31.37],
            '广元': [105.51, 32.28],
            '广州': [113.23, 23.16],
            '贵池': [117.28, 30.39],
            '贵港': [109.36, 23.06],
            '贵阳': [106.71, 26.57],
            '桂林': [110.28, 25.29],
            '桂平': [110.04, 23.22],
            '哈尔滨': [126.63, 45.75],
            '哈密': [93.28, 42.50],
            '海城': [122.43, 40.51],
            '海口': [110.35, 20.02],
            '海拉尔': [119.39, 49.12],
            '海林': [129.21, 44.35],
            '海伦': [126.57, 47.28],
            '海门': [121.15, 31.89],
            '海宁': [120.42, 30.32],
            '邯郸': [114.47, 36.6],
            '韩城': [110.27, 35.28],
            '汉中': [107.01, 33.04],
            '杭州': [120.19, 30.26],
            '蒿城': [114.50, 38.02],
            '合川': [106.15, 30.02],
            '合肥': [117.27, 31.86],
            '合山': [108.52, 23.47],
            '和龙': [129.00, 42.32],
            '和田': [79.55, 37.09],
            '河池': [108.03, 24.42],
            '河间': [116.05, 38.26],
            '河津': [110.41, 35.35],
            '河源': [114.68, 23.73],
            '菏泽': [115.480656, 35.23375],
            '鹤壁': [114.11, 35.54],
            '鹤岗': [130.16, 47.20],
            '鹤山': [112.57, 22.46],
            '黑河': [127.29, 50.14],
            '衡水': [115.72, 37.72],
            '衡阳': [112.37, 26.53],
            '洪湖': [113.27, 29.48],
            '洪江': [109.59, 27.07],
            '侯马': [111.21, 35.37],
            '呼和浩特': [111.65, 40.82],
            '湖州': [120.1, 30.86],
            '葫芦岛': [120.836932, 40.711052],
            '花都': [113.12, 23.23],
            '华阴': [110.05, 34.34],
            '华蓥': [106.44, 30.26],
            '化州': [110.37, 21.39],
            '桦甸': [126.44, 42.58],
            '怀化': [109.58, 27.33],
            '淮安': [119.15, 33.5],
            '淮北': [116.47, 33.57],
            '淮南': [116.58, 32.37],
            '淮阴': [119.02, 33.36],
            '黄骅': [117.21, 38.21],
            '黄山': [118.18, 29.43],
            '黄石': [115.06, 30.12],
            '黄州': [114.52, 30.27],
            '珲春': [130.22, 42.52],
            '辉县': [113.47, 35.27],
            '惠阳': [114.28, 22.48],
            '惠州': [114.4, 23.09],
            '霍林郭勒': [119.38, 45.32],
            '霍州': [111.42, 36.34],
            '鸡西': [130.57, 45.17],
            '吉安': [114.58, 27.07],
            '吉林': [126.57, 43.87],
            '吉首': [109.43, 28.18],
            '即墨': [120.45, 36.38],
            '集安': [126.11, 41.08],
            '集宁': [113.06, 41.02],
            '济南': [117, 36.65],
            '济宁': [116.59, 35.38],
            '济源': [112.35, 35.04],
            '冀州': [115.33, 37.34],
            '佳木斯': [130.22, 46.47],
            '嘉兴': [120.76, 30.77],
            '嘉峪关': [98.289152, 39.77313],
            '简阳': [104.32, 30.24],
            '建德': [119.16, 29.29],
            '建瓯': [118.20, 27.03],
            '建阳': [118.07, 27.21],
            '江都': [119.32, 32.26],
            '江津': [106.16, 29.18],
            '江门': [113.06, 22.61],
            '江山': [118.37, 28.45],
            '江阴': [120.26, 31.91],
            '江油': [104.42, 31.48],
            '姜堰': [120.08, 32.34],
            '胶南': [119.97, 35.88],
            '胶州': [120.03336, 36.264622],
            '焦作': [113.21, 35.24],
            '蛟河': [127.21, 43.42],
            '揭阳': [116.35, 23.55],
            '介休': [111.55, 37.02],
            '界首': [115.21, 33.15],
            '金昌': [102.188043, 38.520089],
            '金华': [119.64, 29.12],
            '金坛': [119.56, 31.74],
            '津市': [111.52, 29.38],
            '锦州': [121.15, 41.13],
            '晋城': [112.51, 35.30],
            '晋江': [118.35, 24.49],
            '晋州': [115.02, 38.02],
            '荆门': [112.12, 31.02],
            '荆沙': [112.16, 30.18],
            '荆州': [112.239741, 30.335165],
            '井冈山': [114.10, 26.34],
            '景德镇': [117.13, 29.17],
            '景洪': [100.48, 22.01],
            '靖江': [120.17, 32.02],
            '九江': [115.97, 29.71],
            '九台': [125.51, 44.09],
            '酒泉': [98.31, 39.44],
            '句容': [119.16, 31.95],
            '喀什': [75.59, 39.30],
            '开封': [114.35, 34.79],
            '开平': [112.40, 22.22],
            '开原': [124.02, 42.32],
            '开远': [103.13, 23.43],
            '凯里': [107.58, 26.35],
            '克拉玛依': [84.77, 45.59],
            '库尔勒': [86.06, 41.68],
            '奎屯': [84.56, 44.27],
            '昆明': [102.73, 25.04],
            '昆山': [120.95, 31.39],
            '廓坊': [116.42, 39.31],
            '拉萨': [91.11, 29.97],
            '莱芜': [117.67, 36.19],
            '莱西': [120.53, 36.86],
            '莱阳': [120.42, 36.58],
            '莱州': [119.942327, 37.177017],
            '兰溪': [119.28, 29.12],
            '兰州': [103.73, 36.03],
            '阆中': [105.58, 31.36],
            '廊坊': [116.7, 39.53],
            '老河口': [111.40, 32.23],
            '乐昌': [113.21, 25.09],
            '乐陵': [117.12, 37.44],
            '乐平': [117.08, 28.58],
            '乐清': [120.58, 28.08],
            '乐山': [103.44, 29.36],
            '雷州': [110.04, 20.54],
            '耒阳': [112.51, 26.24],
            '冷水江': [111.26, 27.42],
            '冷水滩': [111.35, 26.26],
            '醴陵': [113.30, 27.40],
            '丽水': [119.92, 28.45],
            '利川': [108.56, 30.18],
            '溧阳': [119.48, 31.43],
            '连云港': [119.16, 34.59],
            '连州': [112.23, 24.48],
            '涟源': [111.41, 27.41],
            '廉江': [110.17, 21.37],
            '辽阳': [123.12, 41.16],
            '辽源': [125.09, 42.54],
            '聊城': [115.97, 36.45],
            '林州': [113.49, 36.03],
            '临安': [119.72, 30.23],
            '临川': [116.21, 27.59],
            '临汾': [111.5, 36.08],
            '临海': [121.08, 28.51],
            '临河': [107.22, 40.46],
            '临江': [126.53, 41.49],
            '临清': [115.42, 36.51],
            '临夏': [103.12, 35.37],
            '临湘': [113.27, 29.29],
            '临沂': [118.35, 35.05],
            '赁祥': [106.44, 22.07],
            '灵宝': [110.52, 34.31],
            '凌海': [121.21, 41.10],
            '凌源': [119.22, 41.14],
            '浏阳': [113.37, 28.09],
            '柳州': [109.4, 24.33],
            '六安': [116.28, 31.44],
            '六盘水': [104.50, 26.35],
            '龙海': [117.48, 24.26],
            '龙井': [129.26, 42.46],
            '龙口': [120.21, 37.39],
            '龙泉': [119.08, 28.04],
            '龙岩': [117.01, 25.06],
            '娄底': [111.59, 27.44],
            '泸州': [105.39, 28.91],
            '鹿泉': [114.19, 38.04],
            '潞城': [113.14, 36.21],
            '罗定': [111.33, 22.46],
            '洛阳': [112.44, 34.7],
            '漯河': [114.02, 33.33],
            '麻城': [115.01, 31.10],
            '马鞍山': [118.48, 31.56],
            '满洲里': [117.23, 49.35],
            '茂名': [110.88, 21.68],
            '梅河口': [125.40, 42.32],
            '梅州': [116.1, 24.55],
            '汨罗': [113.03, 28.49],
            '密山': [131.50, 45.32],
            '绵阳': [104.73, 31.48],
            '明光': [117.58, 32.47],
            '牡丹江': [129.58, 44.6],
            '南安': [118.23, 24.57],
            '南昌': [115.89, 28.68],
            '南充': [106.110698, 30.837793],
            '南川': [107.05, 29.10],
            '南宫': [115.23, 37.22],
            '南海': [113.09, 23.01],
            '南京': [118.78, 32.04],
            '南宁': [108.33, 22.84],
            '南平': [118.10, 26.38],
            '南通': [121.05, 32.08],
            '南阳': [112.32, 33.00],
            '讷河': [124.51, 48.29],
            '内江': [105.02, 29.36],
            '宁安': [129.28, 44.21],
            '宁波': [121.56, 29.86],
            '宁德': [119.31, 26.39],
            '攀枝花': [101.718637, 26.582347],
            '盘锦': [122.070714, 41.119997],
            '彭州': [103.57, 30.59],
            '蓬莱': [120.75, 37.8],
            '邳州': [117.59, 34.19],
            '平顶山': [113.29, 33.75],
            '平度': [119.97, 36.77],
            '平湖': [121.01, 30.42],
            '平凉': [106.40, 35.32],
            '萍乡': [113.50, 27.37],
            '泊头': [116.34, 38.04],
            '莆田': [119.01, 24.26],
            '濮阳': [115.01, 35.44],
            '浦圻': [113.51, 29.42],
            '普兰店': [121.58, 39.23],
            '普宁': [116.10, 23.18],
            '七台河': [130.49, 45.48],
            '齐齐哈尔': [123.97, 47.33],
            '启乐': [121.39, 31.48],
            '潜江': [112.53, 30.26],
            '钦州': [108.37, 21.57],
            '秦皇岛': [119.57, 39.95],
            '沁阳': [112.57, 35.05],
            '青岛': [120.33, 36.07],
            '青铜峡': [105.59, 37.56],
            '青州': [118.28, 36.42],
            '清远': [113.01, 23.7],
            '清镇': [106.27, 26.33],
            '邛崃': [103.28, 30.26],
            '琼海': [110.28, 19.14],
            '琼山': [110.21, 19.59],
            '曲阜': [116.58, 35.36],
            '曲靖': [103.79, 25.51],
            '衢州': [118.88, 28.97],
            '泉州': [118.58, 24.93],
            '任丘': [116.07, 38.42],
            '日喀则': [88.51, 29.16],
            '日照': [119.46, 35.42],
            '荣成': [122.41, 37.16],
            '如皋': [120.33, 32.23],
            '汝州': [112.50, 34.09],
            '乳山': [121.52, 36.89],
            '瑞安': [120.38, 27.48],
            '瑞昌': [115.38, 29.40],
            '瑞金': [116.01, 25.53],
            '瑞丽': [97.50, 24.00],
            '三河': [117.04, 39.58],
            '三门峡': [111.19, 34.76],
            '三明': [117.36, 26.13],
            '三水': [112.52, 23.10],
            '三亚': [109.511909, 18.252847],
            '沙河': [114.30, 36.51],
            '厦门': [118.1, 24.46],
            '汕头': [116.69, 23.39],
            '汕尾': [115.375279, 22.786211],
            '商丘': [115.38, 34.26],
            '商州': [109.57, 33.52],
            '上海': [121.48, 31.22],
            '上饶': [117.58, 25.27],
            '上虞': [120.52, 30.01],
            '尚志': [127.55, 45.14],
            '韶关': [113.62, 24.84],
            '韶山': [112.29, 27.54],
            '邵武': [117.29, 27.20],
            '邵阳': [111.28, 27.14],
            '绍兴': [120.58, 30.01],
            '深圳': [114.07, 22.62],
            '深州': [115.32, 38.01],
            '沈阳': [123.38, 41.8],
            '十堰': [110.47, 32.40],
            '石河子': [86.00, 44.18],
            '石家庄': [114.48, 38.03],
            '石狮': [118.38, 24.44],
            '石首': [112.24, 29.43],
            '石嘴山': [106.39, 39.04],
            '寿光': [118.73, 36.86],
            '舒兰': [126.57, 44.24],
            '双城': [126.15, 45.22],
            '双鸭山': [131.11, 46.38],
            '顺德': [113.15, 22.50],
            '朔州': [112.26, 39.19],
            '思茅': [100.58, 22.48],
            '四会': [112.41, 23.21],
            '四平': [124.22, 43.10],
            '松原': [124.49, 45.11],
            '苏州': [120.62, 31.32],
            '宿迁': [118.3, 33.96],
            '宿州': [116.58, 33.38],
            '绥芬河': [131.11, 44.25],
            '绥化': [126.59, 46.38],
            '随州': [113.22, 31.42],
            '遂宁': [105.33, 30.31],
            '塔城': [82.59, 46.46],
            '台北': [121.30, 25.03],
            '台山': [112.48, 22.15],
            '台州': [121.420757, 28.656386],
            '太仓': [121.1, 31.45],
            '太原': [112.53, 37.87],
            '泰安': [117.13, 36.18],
            '泰兴': [120.01, 32.10],
            '泰州': [119.9, 32.49],
            '唐山': [118.02, 39.63],
            '洮南': [122.47, 45.20],
            '滕州': [117.09, 35.06],
            '天津': [117.2, 39.13],
            '天门': [113.10, 30.39],
            '天水': [105.42, 34.37],
            '天长': [118.59, 32.41],
            '铁法': [123.32, 42.28],
            '铁力': [128.01, 46.59],
            '铁岭': [123.51, 42.18],
            '通化': [125.56, 41.43],
            '通辽': [122.16, 43.37],
            '通什': [109.31, 18.46],
            '通州': [121.03, 32.05],
            '同江': [132.30, 47.39],
            '桐乡': [120.32, 30.38],
            '铜川': [109.11, 35.09],
            '铜陵': [117.48, 30.56],
            '铜仁': [109.12, 27.43],
            '图们': [129.51, 42.57],
            '吐鲁番': [89.11, 42.54],
            '瓦房店': [121.979603, 39.627114],
            '畹町': [98.04, 24.06],
            '万县': [108.21, 30.50],
            '万源': [108.03, 32.03],
            '威海': [122.1, 37.5],
            '潍坊': [119.1, 36.62],
            '卫辉': [114.03, 35.24],
            '渭南': [109.5, 34.52],
            '温岭': [121.21, 28.22],
            '温州': [120.65, 28.01],
            '文登': [122.05, 37.2],
            '乌海': [106.48, 39.40],
            '乌兰浩特': [122.03, 46.03],
            '乌鲁木齐': [87.68, 43.77],
            '无锡': [120.29, 31.59],
            '吴川': [110.47, 21.26],
            '吴江': [120.63, 31.16],
            '吴忠': [106.11, 37.59],
            '芜湖': [118.38, 31.33],
            '梧州': [111.20, 23.29],
            '五常': [127.11, 44.55],
            '五大连池': [126.07, 48.38],
            '武安': [114.11, 36.42],
            '武冈': [110.37, 26.43],
            '武汉': [114.31, 30.52],
            '武威': [102.39, 37.56],
            '武穴': [115.33, 29.51],
            '武夷山': [118.02, 27.46],
            '舞钢': [113.30, 33.17],
            '西安': [108.95, 34.27],
            '西昌': [102.16, 27.54],
            '西峰': [107.40, 35.45],
            '西宁': [101.74, 36.56],
            '锡林浩特': [116.03, 43.57],
            '仙桃': [113.27, 30.22],
            '咸宁': [114.17, 29.53],
            '咸阳': [108.72, 34.36],
            '香港': [115.12, 21.23],
            '湘潭': [112.91, 27.87],
            '湘乡': [112.31, 27.44],
            '襄樊': [112.08, 32.02],
            '项城': [114.54, 33.26],
            '萧山': [120.16, 30.09],
            '孝感': [113.54, 30.56],
            '孝义': [111.48, 37.08],
            '忻州': [112.43, 38.24],
            '辛集': [115.12, 37.54],
            '新会': [113.01, 22.32],
            '新乐': [114.41, 38.20],
            '新密': [113.22, 34.31],
            '新民': [122.49, 41.59],
            '新泰': [117.45, 35.54],
            '新乡': [113.52, 35.18],
            '新沂': [118.20, 34.22],
            '新余': [114.56, 27.48],
            '新郑': [113.43, 34.24],
            '信阳': [114.04, 32.07],
            '邢台': [114.48, 37.05],
            '荥阳': [113.21, 34.46],
            '兴城': [120.41, 40.37],
            '兴化': [119.50, 32.56],
            '兴宁': [115.43, 24.09],
            '兴平': [108.29, 34.18],
            '兴义': [104.53, 25.05],
            '徐州': [117.2, 34.26],
            '许昌': [113.49, 34.01],
            '宣威': [104.06, 26.13],
            '宣州': [118.44, 30.57],
            '牙克石': [120.40, 49.17],
            '雅安': [102.59, 29.59],
            '烟台': [121.39, 37.52],
            '延安': [109.47, 36.6],
            '延吉': [129.30, 42.54],
            '盐城': [120.13, 33.38],
            '盐在': [120.08, 33.22],
            '兖州': [116.49, 35.32],
            '偃师': [112.47, 34.43],
            '扬中': [119.49, 32.14],
            '扬州': [119.42, 32.39],
            '阳春': [111.48, 22.10],
            '阳江': [111.95, 21.85],
            '阳泉': [113.57, 37.85],
            '伊春': [128.56, 47.42],
            '伊宁': [81.20, 43.55],
            '仪征': [119.10, 32.16],
            '宜宾': [104.56, 29.77],
            '宜昌': [111.3, 30.7],
            '宜城': [112.15, 31.42],
            '宜春': [114.23, 27.47],
            '宜兴': [119.82, 31.36],
            '宜州': [108.40, 24.28],
            '义马': [111.55, 34.43],
            '义乌': [120.06, 29.32],
            '益阳': [112.20, 28.36],
            '银川': [106.27, 38.47],
            '应城': [113.33, 30.57],
            '英德': [113.22, 24.10],
            '鹰潭': [117.03, 28.14],
            '营口': [122.18, 40.65],
            '永安': [117.23, 25.58],
            '永川': [105.53, 29.23],
            '永济': [110.27, 34.52],
            '永康': [120.01, 29.54],
            '永州': [111.37, 26.13],
            '余杭': [120.18, 30.26],
            '余姚': [121.10, 30.02],
            '愉树': [126.32, 44.49],
            '榆次': [112.43, 37.41],
            '榆林': [109.47, 38.18],
            '禹城': [116.39, 36.56],
            '禹州': [113.28, 34.09],
            '玉林': [110.09, 22.38],
            '玉门': [97.35, 39.49],
            '玉溪': [102.52, 24.35],
            '沅江': [112.22, 28.50],
            '原平': [112.42, 38.43],
            '岳阳': [113.09, 29.37],
            '云浮': [112.02, 22.93],
            '运城': [110.59, 35.02],
            '枣阳': [112.44, 32.07],
            '枣庄': [117.57, 34.86],
            '增城': [113.49, 23.18],
            '扎兰屯': [122.47, 48.00],
            '湛江': [110.359377, 21.270708],
            '张家港': [120.555821, 31.875428],
            '张家界': [110.479191, 29.117096],
            '张家口': [114.87, 40.82],
            '张掖': [100.26, 38.56],
            '章丘': [117.53, 36.72],
            '漳平': [117.24, 25.17],
            '漳州': [117.39, 24.31],
            '樟树': [115.32, 28.03],
            '长春': [125.35, 43.88],
            '长葛': [113.47, 34.12],
            '长乐': [119.31, 25.58],
            '长沙': [113, 28.21],
            '长治': [113.08, 36.18],
            '招远': [120.38, 37.35],
            '昭通': [103.42, 27.20],
            '肇东': [125.58, 46.04],
            '肇庆': [112.44, 23.05],
            '镇江': [119.44, 32.2],
            '郑州': [113.65, 34.76],
            '枝城': [111.27, 30.23],
            '中山': [113.38, 22.52],
            '钟祥': [112.34, 31.10],
            '舟山': [122.207216, 29.985295],
            '周口': [114.38, 33.37],
            '株洲': [113.16, 27.83],
            '珠海': [113.52, 22.3],
            '诸城': [119.24, 35.59],
            '诸暨': [120.23, 29.71],
            '驻马店': [114.01, 32.58],
            '庄河': [122.58, 39.41],
            '涿州': [115.59, 39.29],
            '资兴': [113.13, 25.58],
            '资阳': [104.38, 30.09],
            '淄博': [118.05, 36.78],
            '自贡': [104.778442, 29.33903],
            '邹城': [116.58, 35.24],
            '遵化': [117.58, 40.11],
            '遵义': [106.9, 27.7],
        }


class PandasNumpyTypeEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.astype(float).tolist()
        except:
            try:
                return obj.astype(str).tolist()
            except:
                return json.JSONEncoder.default(self, obj)


def json_dumps(data, indent=0):
    return json.dumps(data, indent=indent, cls=PandasNumpyTypeEncoder)


def install_echarts_if_needed():
    """
    Copy all echarts javascripts to jupyter_data_dir
    """
    import shutil
    from jupyter_core.paths import jupyter_data_dir

    nbextension_path = os.path.join(jupyter_data_dir(), NBEXT_NAME)
    pyecharts_signature = os.path.join(nbextension_path,
                                       '.pyecharts.signature')
    if os.path.exists(pyecharts_signature) is False:
        js_folder = template.get_resource_dir(
            os.path.join('templates', 'js'))
        for js_file in os.listdir(js_folder):
            shutil.copy(os.path.join(js_folder, js_file),
                        os.path.join(nbextension_path, js_file))
        __create_pyecharts_signature(pyecharts_signature)


def __create_pyecharts_signature(signature_file):
    with open(signature_file, 'w') as f:
        f.write(
            'Delete me if you want to update echarts.js from pyecharts')
