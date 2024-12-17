<script>
	import * as Form from '$lib/components/ui/form';

	let { form } = $props();
	let { form: formData } = form;
</script>

<div class="flex flex-col w-full items-center">
  <Form.Field {form} name="email" >
    <Form.Control let:attrs>
      <div class="field">
        <Form.Label>E-mail:</Form.Label>
        <input
          {...attrs}
          type="email"
          class="col-span-2"
          placeholder="stay@kitschy.com"
          bind:value={$formData.email}
        />
      </div>
    </Form.Control>
  </Form.Field>
  
  <Form.Field {form} name="password">
    <Form.Control let:attrs>
      <div class="field">
        <Form.Label>Password:</Form.Label>
        <input
          {...attrs}
          class="col-span-2"
          type="password"
          placeholder="**********"
          bind:value={$formData.password}
        />
      </div>
    </Form.Control>
  </Form.Field>
</div>
