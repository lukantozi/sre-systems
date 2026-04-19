from unittest import mock, main, TestCase
import github


class TestUserInfo(TestCase):
    @mock.patch("github.requests.get")
    def test_github(self, get_mock):
        get_mock.return_value.status_code = 200
        get_mock.return_value.json.return_value = {
            "name": "name",
            "public_repos": 1,
            "followers": 1 
        }
        result = github.get_user_info("lukantozi")
        expected_result = {
            "name": "name",
            "repos": 1,
            "followers": 1
        }
        self.assertEqual(result, expected_result)
        get_mock.assert_called_once_with("https://api.github.com/users/lukantozi")

    @mock.patch("github.requests.get")
    def test_github_fail(self, get_mock):
        get_mock.return_value.status_code = 404
        get_mock.return_value.json.return_value = {
            "name": "name",
            "public_repos": 1,
            "followers": 1
        }
        result = github.get_user_info("lukantozi")
        self.assertEqual(result, None)
        get_mock.assert_called_once_with("https://api.github.com/users/lukantozi")


if __name__ == "__main__":
    main()
