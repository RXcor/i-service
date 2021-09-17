export const state = () => {
  return {
    job: {
      id: null,
      data: {
        url: null
      },
      result: {"winners_comments": []},
      // {"vinners_comments": [
      //       {"pk": 17912186890227791, "text": "3/3 взаимно, отвечу 😊 ❤ ❤ ❤", "type": 0, "user": {"pk": 285425453, "username": "teddyifriends", "full_name": "Авторские Teddy 🐻  Welcome .", "is_private": false, "is_verified": false, "is_mentionable": true, "profile_pic_id": "1880092693478864869_285425453", "profile_pic_url": "http://127.0.0.1/proxy-images/fb2302a0-40ed-4792-a95a-d9fa4439d7e0.jpg", "latest_reel_media": 0, "follow_friction_type": 0, "story_reel_media_ids": [], "latest_besties_reel_media": 0}, "status": "Active", "user_id": 285425453, "bit_flags": 0, "created_at": 1538652503, "is_covered": false, "content_type": "comment", "share_enabled": false, "created_at_utc": 1538652503, "has_liked_comment": false, "restricted_status": 0, "comment_like_count": 1, "did_report_as_spam": false, "private_reply_status": 0, "inline_composer_display_condition": "never"},
      //       {"pk": 17912186890227791, "text": "3/3 взаимно, отвечу 😊 ❤ ❤ ❤", "type": 0, "user": {"pk": 285425453, "username": "teddyifriends", "full_name": "Авторские Teddy 🐻  Welcome .", "is_private": false, "is_verified": false, "is_mentionable": true, "profile_pic_id": "1880092693478864869_285425453", "profile_pic_url": "http://127.0.0.1/proxy-images/2d919f64-117d-41f7-85f6-050250ff72bd.jpg", "latest_reel_media": 0, "follow_friction_type": 0, "story_reel_media_ids": [], "latest_besties_reel_media": 0}, "status": "Active", "user_id": 285425453, "bit_flags": 0, "created_at": 1538652503, "is_covered": false, "content_type": "comment", "share_enabled": false, "created_at_utc": 1538652503, "has_liked_comment": false, "restricted_status": 0, "comment_like_count": 1, "did_report_as_spam": false, "private_reply_status": 0, "inline_composer_display_condition": "never"}
      //   ]
      // },
      is_completed: null,
      progress: null,
      type_of: null
    }
  }
};

export const mutations = {
  setJob (state, data) {
    Object.assign(state.job, data)
  },
  setDataUrl (state, data) {
    state.job.data.url = data;
  },
  setTypeOf (state, type) {
    state.job.type_of = type;
  }
};
export const actions = {
  async getJob (state, id) {
    console.log('run getJob')
    const resp = await this.app.$jobService.getById(id);
    state.commit('setJob', resp.data);
  }
};
