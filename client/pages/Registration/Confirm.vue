<template>
	<div>
		<section>
			<div class="bg-gray-200 rounded-md w-full p-1 px-2 mt-2">
				<h1 class="text-sm text-gray-800">来場者登録</h1>
			</div>
		</section>
		<p>内容をご確認ください。</p>
		<ConfirmComponent />
	</div>
</template>

<script>
import ConfirmComponent from "~/components/Registration/ConfirmComponent"
export default {
	components: { ConfirmComponent },
	layout: "portal",
}
</script>
