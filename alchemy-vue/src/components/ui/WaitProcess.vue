<template>
    <div class="wait-process" :class="{show: waitShow}">
        <div>
            <span>{{ waitText }}<div><i></i></div></span>
        </div>
    </div>
</template>

<script>
export default {
  name: 'WaitProcess',
  data() {
  },
  methods: {
  },
  props: {
    waitText: {
        type: String,
        default: 'Wait a moment...'
    },
    waitShow: {
        type: Boolean,
        default: true
    }
  },
}
</script>

<style lang="sass" scoped>
.wait-process
    background: rgba(0, 0, 0, 0.15)
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1)
    backdrop-filter: blur(0px)
    -webkit-backdrop-filter: blur(0px)
    align-items: center
    justify-content: center
    position: absolute
    top: 0
    left: 0
    width: 100%
    height: 100vh
    z-index: 999999
    display: none
    backdrop-filter: blur(3px)
    &.show
        display: flex
    div
        padding: 4px
        background-color: #fff
        display: flex
        flex-direction: column
        span
            border: 1px solid #000
            padding: 20px 40px
            font-family: sans-serif
            font-size: 18px
            font-weight: bold
            background-color: #fff
        div
            height: 6px
            position: relative
            padding: 0
            margin-top: 2px
            i
                display: inline-block
                width: 6px
                height: 6px
                background-color: #000
                border-radius: 50%
                position: absolute
                animation-name: wait-animation
                animation-direction: alternate
                animation-iteration-count: infinite
                animation-duration: 1s
                animation-timing-function: ease-in-out
                left: 100%
@keyframes wait-animation
    from
        left: 0%
    to
        left: 100%

</style>