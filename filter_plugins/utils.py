class FilterModule(object):
    def filters(self):
        return {
            "path_to_regex": self.path_to_regex,
        }

    @staticmethod
    def path_to_regex(data: str) -> str:
        return data.replace('/', r'\/').replace('*', r'\*').replace('.', r'\.')
