# ユーザ定義
from app.common import utils
from flask import (Blueprint, Flask, abort, jsonify, make_response, request,
                   send_file, Response)
from flask_restful import Api, Resource, abort, reqparse, url_for
from datetime import date, datetime
from typing import Optional, Any
import json
from app.common.geo import Geo
from app.common.locus import Locus
from app.common.user import User

api_bp = Blueprint("locus", __name__)
api = Api(api_bp)

class LocusQuery(Resource):
    def post(self) -> Response:
        """
            ユーザーが軌跡を送る
            body: { locus: [
                    {latitude[float], longitude[float]}, 
                    {latitude[float], longitude[float]}, 
                    ...
                ],
                user_id[int]
            }
            response: { users: [
                {id[int], name[str], latitude[float], longitude[float])},
                {id[int], name[str], latitude[float], longitude[float])}
            ] }
        """
        try:
            request_json_data: Any | None = request.get_json(force=True)
            print(request_json_data)
        except Exception as e:
            # abort(500, message="入力パラメータの解析失敗")
            raise e  # DEBUG: デバッグ用

        user_id = request_json_data['user_id']
        geos:list[Geo] = [Geo(latitude=geo['latitude'], longitude=geo['longitude']) for geo in request_json_data['locus']]
        locus = Locus(geos=geos)
        locus_id = utils.put_user_locus(user_id, locus)
        locus.locus_id = locus_id
        left_top_geo, right_bottom_geo = locus.get_rectangle()
        users:list[User] = utils.get_near_users(left_top_geo, right_bottom_geo)
        users = list(map(lambda user: user.dump(), (filter(lambda user: locus.is_in(user.geo), users))))
        result: dict = {"users": users}
        response: Response = jsonify(result)
        response.status_code = 200
        return response

    def get(self, locus_id:int) -> Response:
        """
            囲われた軌跡を取得する
            path_query: locus_id[int]
            response:  {
                locus:  [
                    {latitude[float], longitude[float]},
                    {latitude[float], longitude[float]},
                    …
                ],
                user_id[int], 
                user_name[str] 
            }
        """
        locus:Locus = utils.get_locus_by_id(locus_id)
        result: dict = {"locus": locus.dump()}
        response: Response = jsonify(result)
        response.status_code = 200
        return response

api.add_resource(LocusQuery, "/locus", "/locus/<int:locus_id>")
