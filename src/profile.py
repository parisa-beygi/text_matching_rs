class ProfileDictionary(object):
    def __init__(self):
        self.dict = {}

    def get_dict(self):
        return [self.dict[id] for id in self.dict]
        # for id in self.dict:
        #     yield self.dict[id]

    def get_profile(self, id):
        if id not in self.dict:
            p = Profile(id)
            self.dict[id] = p
        return self.dict[id]



class Profile(object):
    def __init__(self, id):
        self.profile_id = id
        self.text_list = []
        self.other_profile_id_list = []
        self.rating_list = []

    def num_of_reviews(self):
        return len(self.text_list)

    def get_review_details(self, index):
        return self.text_list[index], self.rating_list[index], self.other_profile_id_list[index]


    def get_first_text(self):
        return self.text_list[0]

    def append_text(self, rev):
        self.text_list.append(rev)

    def append_other_profile_id(self, id):
        self.other_profile_id_list.append(id)

    def append_rating_list(self, rating):
        self.rating_list.append(rating)

    def update(self, rev, other_profile_id, rating):
        self.append_text(rev)
        self.append_other_profile_id(other_profile_id)
        self.append_rating_list(rating)