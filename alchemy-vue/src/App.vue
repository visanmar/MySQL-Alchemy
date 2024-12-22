<template>
  <div class="task-list-container">
    <TaskList></TaskList>
  </div>
</template>

<script>
import TaskList from '@/components/TasksList.vue'

export default {
  name: 'App',
  components: {
    TaskList
  }
}
</script>

<style lang="sass">
*
  box-sizing: border-box
  outline: none
  font-family: sans-serif
  font-size: 16px
body
  padding: 10px
  .task-list-container
    width: 800px
    margin: 0 auto
</style>
