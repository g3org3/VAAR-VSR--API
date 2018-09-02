;;for vdu in vdus
(and
  (< vdu.mem_size 600 MB )
  (> vdu.num_cpus 0 )
  (< vdu.num_cpus 6 )
)
;;endfor

;;for vnf_i in vnfs
(and
  (< vnf_i.address 10.100.0.150 )
  (> vnf_i.address 10.100.0.100 )
  (< vnf_i.nsh_aware 1 )
)
;;endfor