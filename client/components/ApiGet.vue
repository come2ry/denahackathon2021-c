<script>
import ApiClientBase from '@/store/api-client-base.js'
export default {
  name: 'ApiClientBase',
  components: { ApiClientBase },
  computed: {
    isViewMode() {
      return this.$store.locus
    },
  },
}
</script>
