# ユーザ定義
from app.common import utils
from flask import (Blueprint, Flask, abort, jsonify, make_response, request,
                   send_file, Response)
from flask_restful import Api, Resource, abort, reqparse, url_for
from datetime import date, datetime
from typing import Optional, Any
import json
# from app.common.geo import Geo
# from app.common.locus import Locus
# from app.common.user import User
from database import session
from app import models

api_bp = Blueprint("geo", __name__)
api = Api(api_bp)


class GeoQuery(Resource):
    def post(self) -> Response:
        """
            ユーザーが位置情報を定期アップロードする
            body : { geo: { user_id[int]  latitude[float], longitude[float] } }
            response: { locus_id[int], user_id(囲った人), username[str], datetime }
        """
        try:
            request_json_data: Any | None = request.get_json(force=True)
            print(request_json_data)
        except Exception as e:
            # abort(500, message="入力パラメータの解析失敗")
            raise e  # DEBUG: デバッグ用

        user_id = request_json_data["user_id"]
        user = session.query(models.User).filter(
            models.User.id == user_id).one_or_none()
        latitude = request_json_data["latitude"]
        longitude = request_json_data["longitude"]
        new_geo = models.Geo(
            latlng=f"POINT ({latitude} {longitude})",
        )
        user = session.query(models.User).filter(
            models.User.id == user_id).one_or_none()
        new_geo.user = user

        session.add(new_geo)
        session.commit()
        # utils.put_user_geo(request_json_data['user_id'], models.Geo(
        #     latitude=request_json_data['latitude'], longitude=request_json_data['longitude']))
        locus_notify: models.Locus = utils.get_locus_by_victim(user_id)

        result: dict = {
            'locus_id': locus_notify.locus_id,
            'user_id': locus_notify.locus.user_id,
            'user_name': locus_notify.locus.user.user_name,
            'datetime': locus_notify.created_at
        }
        # result: dict = {k: v for k, v in locus.dump().items() if k != "geos"}
        response: Response = jsonify(result)
        response.status_code = 200
        return response

    def get(self) -> Response:
        """
            ユーザーが位置情報を定期取得する
            query : top[float], left[float], bottom[float], right[float]
            # top, bottom: latitude
            # left, right: longitude
            response:  { users:[
                {id[int], username[str], latitude[float], longitude[float]},
                {id[int], username[str], latitude[float], longitude[float]}
            ] }
        """

        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "top",
                required=True,
                type=float,
                location='args')
            parser.add_argument(
                "left",
                required=True,
                type=float,
                location='args')
            parser.add_argument(
                "bottom",
                required=True,
                type=float,
                location='args')
            parser.add_argument(
                "right",
                required=True,
                type=float,
                location='args')
            args = parser.parse_args(strict=True)
            print(args)
        except Exception as e:
            #     # abort(500, message="入力パラメータの解析失敗")
            raise e  # DEBUG: デバッグ用

        users: list[User] = utils.get_user_geos(Geo(latitude=args.top, longitude=args.left), Geo(
            latitude=args.bottom, longitude=args.right))
        result: dict = {"users": [user.dump() for user in users]}
        response: Response = jsonify(result)
        response.status_code = 200
        return response


api.add_resource(GeoQuery, "/geo")
