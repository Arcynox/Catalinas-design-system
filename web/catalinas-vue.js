/* Catalinas Design System - Vue 3 bindings (generated)
   Requiere Vue 3 global. Uso:
   Object.assign(app.components, CatalinasVue) */



// badge-tooltip-kbd-avatar

export const CatBadge = (props) => h('span', { class: 'cat-badge' + (props.tone ? ' ' + props.tone : '') },
  [props.dot ? h('span', { class: 'dot' }) : null], props.default);

export const CatAvatar = (props) => h('span', { class: 'cat-avatar' },
  props.src ? h('img', { src: props.src }) : props.initials,
  props.online ? h('span', { class: 'presence' }) : null);

// button

export const CatButton = (props, ctx) => h('button', {
  class: ['cat-btn', props.variant, props.size !== 'md' ? props.size : null,
          props.loading ? 'loading' : null],
  disabled: props.disabled,
  onClick: () => ctx.emit('click')
}, [props.icon, ctx.slots.default ? ctx.slots.default() : null]);

// card-toast

export const CatCard = (props) => h('div', { class: 'cat-card ' + (props.level || '') }, props.default);

export const CatToast = (props, ctx) => h('div', { class: 'cat-toast ' + (props.tone === 'info' ? '' : props.tone) }, [
  h('span', { class: 't-icon' }),
  h('div', { style: 'flex:1' }, [h('b', props.title)]),
  h('button', { class: 't-close', onClick: () => ctx.emit('close') }, 'x')
]);

// switch

export const CatSwitch = (props, ctx) => h('label', { class: 'cat-switch' }, [
  h('input', { type: 'checkbox', checked: props.checked, disabled: props.disabled,
    onChange: e => ctx.emit('change', e.target.checked) }),
  h('span', { class: 'track' })
]);
