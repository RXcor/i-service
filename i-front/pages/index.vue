<template>
  <v-main>

  <v-card
    tyle="opacity: 0.9;"
    elevation = 10
  >
    <v-tabs
      v-model="tabs"
      centered
    >
      <v-tab
        v-for="n in 3"
        :key="n"
      >
        {{ titles[n] }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tabs">
      <v-tab-item>
        <v-card flat>
          <v-card-text>
              <v-text-field
                label="Ссылка на пост"
                placeholder="instagram.com/p/BoeeKVxlrfH/"
                outlined
                @input="setDataUrl"
              ></v-text-field>

              <div style="height: 12px;">
                <v-progress-linear
                  v-show="viewProgress || delayViewProgress"
                  color="blue darken-2"
                  buffer-value="0"
                  :value="job.progress"
                  stream
                ></v-progress-linear>
              </div>

            <v-chip-group
              column
              multiple
              v-model="selectTags"
            >
            <v-chip
              filter
              v-for="tag in tags"
              :key="tag.param"
            >
              {{ tag.text }}
            </v-chip>
            </v-chip-group>
            <v-card
              class="d-flex align-end flex-column"
              elevation="0"
            >

            <v-btn
              x-large
              class="d-flex align-end flex-column"
              @click="newRaffle">
              Запуск
            </v-btn>
            </v-card>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="headline">
            An awesome title
          </v-card-title>
          <v-card-text>
            <p>
              Duis lobortis massa imperdiet quam. Donec vitae orci sed dolor rutrum auctor. Vestibulum facilisis, purus nec pulvinar iaculis, ligula mi congue nunc, vitae euismod ligula urna in dolor. Praesent congue erat at massa.
            </p>
            <p>
              Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Pellentesque egestas, neque sit amet convallis pulvinar, justo nulla eleifend augue, ac auctor orci leo non est. Etiam sit amet orci eget eros faucibus tincidunt. Donec sodales sagittis magna.
            </p>
            <p class="mb-0">
              Ut leo. Suspendisse potenti. Duis vel nibh at velit scelerisque suscipit. Fusce pharetra convallis urna.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-title class="headline">
            An even better title
          </v-card-title>
          <v-card-text>
            <p>
              Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Sed hendrerit. Maecenas malesuada. Vestibulum ullamcorper mauris at ligula. Proin faucibus arcu quis ante.
            </p>
            <p class="mb-0">
              Etiam vitae tortor. Curabitur ullamcorper ultricies nisi. Sed magna purus, fermentum eu, tincidunt eu, varius ut, felis. Aliquam lobortis. Suspendisse potenti.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
  </v-card>

  <br />

  <v-container fluid>
    <v-row
      align="center"
      justify="center"
      v-if="job.result.winners_comments.length > 0">

      <span class="text-h4" style="padding: 20px;">
        Победители розыгрыша
      </span>

    </v-row>
    <v-row>
      <v-col
        v-for="(item, i) in job.result.winners_comments"
        :key="i"
        cols="12"
        sm="6"

      >
        <v-card
          dark
        >
          <div class="d-flex flex-no-wrap justify-space-between">
            <div>
              <v-card-title
                class="text-h5"
                v-text="item.user.username"
              ></v-card-title>
              <v-card-subtitle v-text="item.text"></v-card-subtitle>
            </div>

            <v-avatar
              class="ma-3"
              size="125"
              tile
            >
              <v-img :src="item.user.profile_pic_url"></v-img>
            </v-avatar>
          </div>
        </v-card>
        </v-col>
      </v-row>
    </v-container>

  </v-main>

</template>
<script>
  import { mapState, mapActions, mapMutations } from 'vuex'
  export default {

    data () {
      return {
        delayViewProgress: false,
        selectTags: null,
        tags: [
          {
            param: 'exclude_masfollowers',
            text: 'Исключить масфолловеров',
            value: true
          },
          {
            param: 'min_media_count',
            text: 'Профили с кол. постов > 5',
            value: 6
          },
          {
            param: 'winners_is_folowers',
            text: 'Подписчики',
            value: true,
          },
          {
            param: 'winners_count',
            text: '3 победителя',
            value: 3
          }
        ],
        titles: ['', 'Розыгрыш', 'Лайктаймы', 'Че то еще'],
        tabs: null,
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
    auth: false,
    layout: 'promo',
    computed: {
      ...mapState('job', ['job']),
      viewProgress(){
        if(typeof this.job.progress == 'number' && this.job.progress < 100) {
          return true
        } else if (this.job.progress == 100) {
            this.delayViewProgress = true
            setTimeout(() => {this.delayViewProgress = false}, 2000)
            return false
        } else {
          return false
        }
      }


    },
    methods: {
      ...mapMutations('job', ['setDataUrl', 'setType']),
      ...mapActions('job', ['getJob']),

      async newRaffle() {
        var selectParams = {}
        if(this.selectTags != null) {
          this.selectTags.forEach(i => selectParams[[this.tags[i].param]] = this.tags[i].value)
        }

        var job = { ...this.job }
        job.type_of = 6
        Object.assign(job.data, selectParams)
        console.log(job)

        const createResp = await this.$jobService.createJob(job).catch(
          (error) => error.response
        );
        if (createResp.status === 201) {
          await this.getJob(createResp.data.id);
          this.delayViewProgress = true
          let id = this.job.id
          let timerJob = setInterval( () => {
            this.getJob(id);
            if (this.job.progress == 100) {
              clearInterval(timerJob);
              console.log('выполнение закончено')
            }
          }, 2000);

        } else if (createResp.status === 400) {
          console.log(createResp.data);
        } else {
          createResp.data.validation_errors
        }
      },

    }

    // page component definitions
  }
</script>
