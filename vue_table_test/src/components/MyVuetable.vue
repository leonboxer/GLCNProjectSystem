<template>
    <div>
        <vuetable ref="vuetable"
                  api-url="https://vuetable.ratiw.net/api/users"
                  :fields="fields"
                  :sort-order="sortOrder"
                  data-path="data"
                  :per-page="5"
                  pagination-path=""
                  @vuetable:pagination-data="onPaginationData"
        ></vuetable>

        <div class="pagination ui basic segment grid">
            <vuetable-pagination-info ref="paginationInfo"
            ></vuetable-pagination-info>

            <vuetable-pagination ref="pagination"
                                 @vuetable-pagination:change-page="onChangePage"
            ></vuetable-pagination>
        </div>
    </div>
</template>
<script>
    import Vuetable from "vuetable-2/src/components/Vuetable";
    import VuetablePagination from "vuetable-2/src/components/VuetablePagination";
    import VuetablePaginationInfo from "vuetable-2/src/components/VuetablePaginationInfo";
    import FieldsDef from "./FieldsDef.js";

    export default {
        name: "MyVuetable",
        components: {
            Vuetable,
            VuetablePagination,
            VuetablePaginationInfo
        },
        data() {
            return {
                fields: FieldsDef,
                sortOrder: [
                    {
                        field: "email",
                        direction: "asc"
                    }
                ]
            };
        },
        methods: {
            onPaginationData(paginationData) {
                this.$refs.pagination.setPaginationData(paginationData);
                this.$refs.paginationInfo.setPaginationData(paginationData);
            },
            onChangePage(page) {
                this.$refs.vuetable.changePage(page);
            }
        }
    };
</script>

<style>
    .pagination {
        margin-top: 1rem;
    }

    .vuetable-head-wrapper table.vuetable th.sortable {
        cursor: pointer
    }
</style>
