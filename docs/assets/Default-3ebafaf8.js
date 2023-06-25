import{r as A,I as ie,o as re,w as ce,a as q,b as D,p as O,i as F,c as v,d as z,g as ve,s as K,e as U,f as pe,h as V,j as fe,k as W,l as x,m as de,n as X,q as Y,t as G,u as me,v as ye,x as ge}from"./index-caa0a76e.js";import{m as J,a as he,u as Q}from"./tag-b15d8746.js";function _e(e){const i=A(),t=A();if(ie){const s=new ResizeObserver(o=>{e==null||e(o,s),o.length&&(t.value=o[0].contentRect)});re(()=>{s.disconnect()}),ce(i,(o,l)=>{l&&(s.unobserve(q(l)),t.value=void 0),o&&s.observe(q(o))},{flush:"post"})}return{resizeRef:i,contentRect:D(t)}}const P=Symbol.for("vuetify:layout"),xe=Symbol.for("vuetify:layout-item"),Z=1e3,be=O({overlaps:{type:Array,default:()=>[]},fullHeight:Boolean},"layout");function Ie(){const e=F(P);if(!e)throw new Error("[Vuetify] Could not find injected layout");return{getLayoutItem:e.getLayoutItem,mainRect:e.mainRect,mainStyles:e.mainStyles}}const we=(e,i,t,s)=>{let o={top:0,left:0,right:0,bottom:0};const l=[{id:"",layer:{...o}}];for(const r of e){const d=i.get(r),y=t.get(r),_=s.get(r);if(!d||!y||!_)continue;const g={...o,[d.value]:parseInt(o[d.value],10)+(_.value?parseInt(y.value,10):0)};l.push({id:r,layer:g}),o=g}return l};function Re(e){const i=F(P,null),t=v(()=>i?i.rootZIndex.value-100:Z),s=A([]),o=z(new Map),l=z(new Map),r=z(new Map),d=z(new Map),y=z(new Map),{resizeRef:_,contentRect:g}=_e(),ee=v(()=>{const a=new Map,p=e.overlaps??[];for(const n of p.filter(c=>c.includes(":"))){const[c,u]=n.split(":");if(!s.value.includes(c)||!s.value.includes(u))continue;const m=o.get(c),h=o.get(u),R=l.get(c),S=l.get(u);!m||!h||!R||!S||(a.set(u,{position:m.value,amount:parseInt(R.value,10)}),a.set(c,{position:h.value,amount:-parseInt(S.value,10)}))}return a}),b=v(()=>{const a=[...new Set([...r.values()].map(n=>n.value))].sort((n,c)=>n-c),p=[];for(const n of a){const c=s.value.filter(u=>{var m;return((m=r.get(u))==null?void 0:m.value)===n});p.push(...c)}return we(p,o,l,d)}),T=v(()=>!Array.from(y.values()).some(a=>a.value)),I=v(()=>b.value[b.value.length-1].layer),te=v(()=>({"--v-layout-left":V(I.value.left),"--v-layout-right":V(I.value.right),"--v-layout-top":V(I.value.top),"--v-layout-bottom":V(I.value.bottom),...T.value?void 0:{transition:"none"}})),w=v(()=>b.value.slice(1).map((a,p)=>{let{id:n}=a;const{layer:c}=b.value[p],u=l.get(n),m=o.get(n);return{id:n,...c,size:Number(u.value),position:m.value}})),E=a=>w.value.find(p=>p.id===a),L=ve("createLayout"),k=K(!1);U(()=>{k.value=!0}),pe(P,{register:(a,p)=>{let{id:n,order:c,position:u,layoutSize:m,elementSize:h,active:R,disableTransitions:S,absolute:se}=p;r.set(n,c),o.set(n,u),l.set(n,m),d.set(n,R),S&&y.set(n,S);const H=fe(xe,L==null?void 0:L.vnode).indexOf(a);H>-1?s.value.splice(H,0,n):s.value.push(n);const N=v(()=>w.value.findIndex($=>$.id===n)),M=v(()=>t.value+b.value.length*2-N.value*2),ae=v(()=>{const $=u.value==="left"||u.value==="right",B=u.value==="right",ue=u.value==="bottom",j={[u.value]:0,zIndex:M.value,transform:`translate${$?"X":"Y"}(${(R.value?0:-110)*(B||ue?-1:1)}%)`,position:se.value||t.value!==Z?"absolute":"fixed",...T.value?void 0:{transition:"none"}};if(!k.value)return j;const f=w.value[N.value];if(!f)throw new Error(`[Vuetify] Could not find layout item "${n}"`);const C=ee.value.get(n);return C&&(f[C.position]+=C.amount),{...j,height:$?`calc(100% - ${f.top}px - ${f.bottom}px)`:h.value?`${h.value}px`:void 0,left:B?void 0:`${f.left}px`,right:B?`${f.right}px`:void 0,top:u.value!=="bottom"?`${f.top}px`:void 0,bottom:u.value!=="top"?`${f.bottom}px`:void 0,width:$?h.value?`${h.value}px`:void 0:`calc(100% - ${f.left}px - ${f.right}px)`}}),le=v(()=>({zIndex:M.value-1}));return{layoutItemStyles:ae,layoutItemScrimStyles:le,zIndex:M}},unregister:a=>{r.delete(a),o.delete(a),l.delete(a),d.delete(a),y.delete(a),s.value=s.value.filter(p=>p!==a)},mainRect:I,mainStyles:te,getLayoutItem:E,items:w,layoutRect:g,rootZIndex:t});const oe=v(()=>["v-layout",{"v-layout--full-height":e.fullHeight}]),ne=v(()=>({zIndex:t.value,position:i?"relative":void 0,overflow:i?"hidden":void 0}));return{layoutClasses:oe,layoutStyles:ne,getLayoutItem:E,items:w,layoutRect:g,layoutRef:_}}function Se(){const e=K(!1);return U(()=>{window.requestAnimationFrame(()=>{e.value=!0})}),{ssrBootStyles:v(()=>e.value?void 0:{transition:"none !important"}),isBooted:D(e)}}const $e=O({scrollable:Boolean,...J(),...he({tag:"main"})},"VMain"),ze=W()({name:"VMain",props:$e(),setup(e,i){let{slots:t}=i;const{mainStyles:s}=Ie(),{ssrBootStyles:o}=Se();return Q(()=>x(e.tag,{class:["v-main",{"v-main--scrollable":e.scrollable},e.class],style:[s.value,o.value,e.style]},{default:()=>{var l,r;return[e.scrollable?x("div",{class:"v-main__scroller"},[(l=t.default)==null?void 0:l.call(t)]):(r=t.default)==null?void 0:r.call(t)]}})),{}}}),Ve={__name:"View",setup(e){return(i,t)=>{const s=de("router-view");return X(),Y(ze,null,{default:G(()=>[x(s)]),_:1})}}};const Le=O({...J(),...be({fullHeight:!0}),...me()},"VApp"),Me=W()({name:"VApp",props:Le(),setup(e,i){let{slots:t}=i;const s=ye(e),{layoutClasses:o,layoutStyles:l,getLayoutItem:r,items:d,layoutRef:y}=Re(e),{rtlClasses:_}=ge();return Q(()=>{var g;return x("div",{ref:y,class:["v-application",s.themeClasses.value,o.value,_.value,e.class],style:[l.value,e.style]},[x("div",{class:"v-application__wrap"},[(g=t.default)==null?void 0:g.call(t)])])}),{getLayoutItem:r,items:d,theme:s}}}),Pe={__name:"Default",setup(e){return(i,t)=>(X(),Y(Me,null,{default:G(()=>[x(Ve)]),_:1}))}};export{Pe as default};
