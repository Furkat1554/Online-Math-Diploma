
class ExpressionRequestResult:
    expression = ""

    def __init__(self):
        pass

    def get_json(self):
        result = {
            "expression": self.expression
        }
        return result


class ResultResponse:
    is_true_answer = False

    def __init__(self):
        pass

    def get_json(self):
        result = {
            "isTrueAnswer": self.is_true_answer
        }
        return result
