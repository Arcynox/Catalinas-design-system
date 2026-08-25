/* Catalinas Design System — React bindings (generated)
   Uso: <CatButton variant="danger">Eliminar</CatButton>
   Requiere catalinas.css en la app. */



// alert-banner
const I = {
  info: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4"><circle cx="12" cy="12" r="9" /><path d="M12 8h.01M12 11v5" strokeLinecap="round" /></svg>,
  success: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.8" strokeLinecap="round"><path d="M5 13l4 4 10-10" /></svg>,
  warning: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round"><path d="M12 4L2 20h20z" /><path d="M12 10v4m0 3h.01" /></svg>,
  danger: <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round"><path d="M6 6l12 12M18 6L6 18" /></svg>,
};
export function CatAlert({ tone = "info", title, message, onClose }) {
  return (
    <div className={"cat-alert " + tone}>
      <span className="a-icon" aria-hidden>{I[tone] || I.info}</span>
      <div className="a-body"><b>{title}</b><span>{message}</span></div>
      {onClose && <button className="t-close" data-cat-dismiss=".cat-alert" onClick={onClose}>x</button>}
    </div>
  );
}

// badge-tooltip-kbd-avatar
export function CatBadge({ tone, dot, children }) {
  return <span className={"cat-badge" + (tone ? " " + tone : "")}>{dot && <span className="dot" />}{children}</span>;
}

export function CatTooltip({ label, children }) {
  return <span data-cat-tooltip={label}>{children}</span>;
}

export function Kbd({ children }) { return <kbd className="cat-kbd">{children}</kbd>; }

export function CatAvatar({ initials, src, online }) {
  return (
    <span className="cat-avatar">
      {src ? <img src={src} alt="" /> : initials}
      {online && <span className="presence" />}
    </span>
  );
}

// button
export function CatButton({ variant = "primary", size, icon, loading, className = "", children, ...p }) {
  const cls = ["cat-btn", variant, size && size !== "md" ? size : "", loading ? "loading" : "", className].filter(Boolean).join(" ");
  return <button {...p} className={cls}>{icon}{children}</button>;
}

// card-toast
export function CatCard({ level = "content", className = "", children, ...p }) {
  return <div {...p} className={"cat-card " + level + " " + className}>{children}</div>;
}

export function CatToasts({ children }) { return <div className="cat-toasts">{children}</div>; }
export function CatToast({ tone = "info", title, onClose }) {
  return (
    <div className={"cat-toast " + (tone === "info" ? "" : tone)}>
      <span className="t-icon" />
      <div style={{ flex: 1 }}><b>{title}</b></div>
      {onClose && <button className="t-close" data-cat-dismiss=".cat-toast" onClick={onClose}>x</button>}
    </div>
  );
}

// checkbox-radio
export function CatCheck({ children, ...p }) {
  return <label className="cat-check"><input type="checkbox" {...p} /><span className="box" />{children}</label>;
}
export function CatRadio({ name, children, ...p }) {
  return <label className="cat-radio"><input type="radio" name={name} {...p} /><span className="box" />{children}</label>;
}

// input
export function CatField({ label, icon, error, textarea, select, options = [], className = "", ...p }) {
  return (
    <div className={"cat-field" + (error ? " is-error" : "") + " " + className}>
      {label && <label className="cat-label">{label}</label>}
      <div className={"cat-input" + (icon ? " has-icon" : "")}>
        {icon && <span className="cat-icon">{icon}</span>}
        {textarea ? <textarea className="el" {...p} />
          : select ? <select className="el" {...p}>{options.map(o => <option key={o}>{o}</option>)}</select>
          : <input className="el" {...p} />}
      </div>
      {error && <span className="field-msg">{error}</span>}
    </div>
  );
}

// segmented
export function CatSegmented({ name, options }) {
  return (
    <div className="cat-segmented">
      {options.map((o, i) => (
        <label key={i}><input type="radio" name={name} defaultChecked={i === 0} /><span>{o}</span></label>
      ))}
    </div>
  );
}

// slider
export function CatSlider({ accent, ...p }) {
  return <input type="range" className={"cat-slider" + (accent ? " accent" : "")} {...p} />;
}

// switch
export function CatSwitch({ defaultChecked, disabled, onChange }) {
  return (
    <label className="cat-switch">
      <input type="checkbox" defaultChecked={defaultChecked} disabled={disabled} onChange={onChange} />
      <span className="track" />
    </label>
  );
}

// tabs
export function CatTabs({ tabs, groupId }) {
  return (
    <div className="cat-tabs" data-cat-tabs={groupId || undefined} role="tablist">
      {tabs.map((t, i) => (
        <button key={i} role="tab" aria-selected={i === 0}
          data-cat-tab={t.id}
          className={"cat-tab" + (i === 0 ? " is-active" : "")}>{t.label}</button>
      ))}
    </div>
  );
}


export const tokens = window.CATALINAS_TOKENS; // si cargas docs/tokens.js
