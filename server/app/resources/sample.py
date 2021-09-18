# ユーザ定義
from app.common import utils, datastore
from flask import (Blueprint, Flask, abort, jsonify, make_response, request,
                   send_file, Response)
from flask_restful import Api, Resource, abort, reqparse, url_for
from datetime import date, datetime
from typing import Optional, Any
import json

api_bp = Blueprint("sample", __name__)
api = Api(api_bp)


class SampleUserQuery(Resource):

    def get(self) -> Response:
        """SampleUserQueryのGETメソッド
        SAMPLE_USERSからクエリパラメータに条件を指定してユーザを取得する

        Args: 以下のkeyで検索をかける. key同士はORで検索.
            github_id (str | None): github_idで検索.
            birthday (str("%Y-%m-%d") | None): birthdayで検索.
            role (str("backend" | "frontend") | None): roleで検索.

        Returns:
            Response: [
                {
                    "github_id": string,
                    "birthday": str("%Y-%m-%d") | None,
                    "role": string("backend" | "frontend"),
                },
                ...
            ]
        """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "github_id",
                required=False,
                type=str,
                location='args')
            parser.add_argument(
                "birthday",
                required=False,
                type=Optional[str],
                location='args')
            parser.add_argument(
                "role",
                required=False,
                type=Optional[str],
                location='args')
            # NOTE: strict=Trueで`github_id`, `birthday`,
            # `role`以外が渡されたらエラーをなげるようにする
            args = parser.parse_args(strict=True)
        except Exception as e:
            # abort(500, message="入力パラメータの解析失敗")
            raise e  # DEBUG: デバッグ用

        try:
            # 全取得
            print(args)
            for key, value in args.copy().items():
                if value is not None:
                    break
            else:
                response: Response = jsonify(
                    list(datastore.SAMPLE_USERS.values()))
                response.status_code = 200
                return response

            result: list[dict] = []
            # parametersで追加検索
            if len(args) > 0:
                for arg_key, arg_value in args.items():
                    for s_id, s_user in datastore.SAMPLE_USERS.items():
                        s_user_value: dict | None = s_user.get(arg_key)
                        if s_user_value is None:
                            continue
                        if s_user_value == arg_value:
                            result.append(s_user)
        except Exception as e:
            # abort(500, message="検索失敗")
            raise e  # DEBUG: デバッグ用

        response: Response = jsonify(result)
        response.status_code = 200
        return response


class SampleUser(Resource):

    def get(self, id: Optional[int] = None) -> Response:
        """SampleUserのGETメソッド
        SAMPLE_USERSからパスパラメータにidを指定してユーザを取得する

        Args:
            id (int | None): idで検索する.

        Returns:
            Response: [
                {
                    "github_id": string,
                    "birthday": str("%Y-%m-%d") | None,
                    "role": string("backend" | "frontend"),
                },
                ...
            ]
        """
        try:
            print(id)
            # 全取得
            if id is None:
                response: Response = jsonify(datastore.SAMPLE_USERS.values())
                response.status_code = 200
                return response

            result: list[dict] = []
            # idで検索
            if id is not None:
                s_user: dict | None = datastore.SAMPLE_USERS.get(id, None)
                if s_user is None:
                    abort(404, message=f"id {id} doesn't exist")
                result.append(s_user)
        except Exception as e:
            # abort(500, message="検索失敗")
            raise e  # DEBUG: デバッグ用

        response: Response = jsonify(result)
        response.status_code = 200
        return response

    def post(self) -> Response:
        """SampleUserのPOSTメソッド
        クエリパラメータでユーザ情報を指定してユーザをSAMPLE_USERSに作成する

        Args:
            github_id (str | None): githubのid.
            birthday (str("%Y-%m-%d") | None): 誕生日. 例) "1998-12-09"
            role (str("backend" | "frontend") | None): 役割

        Returns:
            Response: {
                "github_id": string,
                "birthday": str("%Y-%m-%d") | None,
                "role": string("backend" | "frontend"),
            }
        """
        try:
            request_json_data: Any | None = request.get_json(force=True)
            # 必須項目
            github_id: str = request_json_data["github_id"]
            role: str = request_json_data["role"]
            # 選択項目
            _birthday_str: str | None = request_json_data.get("birthday", None)
            _dt: datetime = datetime.strptime(
                _birthday_str, "%Y-%m-%d")
            birthday: date = date(_dt.year, _dt.month, _dt.day)
        except Exception as e:
            # abort(500, message="入力パラメータの解析失敗")
            raise e  # DEBUG: デバッグ用

        try:
            new_user_data: dict = {
                "github_id": github_id,
                "birthday": birthday.strftime('%Y-%m-%d'),
                "role": role,
            }
            utils.create_sample_user(new_user_data)
        except Exception as e:
            # abort(500, message=f"github_id {github_id} failed to create")
            raise e  # DEBUG: デバッグ用

        response: Response = jsonify(new_user_data)
        response.status_code = 200
        return response


api.add_resource(SampleUserQuery, "/sample/users")
api.add_resource(SampleUser, "/sample/users", "/sample/users/<int:id>")
