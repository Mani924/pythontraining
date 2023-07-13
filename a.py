
rego
package k8spspallowedusers

violation[_] {
  fields := ["runAsUser", "runAsGroup", "supplementalGroups", "fsGroup"]
  field := fields[_]
  container := input_containers[_]
  not is_exempt(container)
  get_type_violation(field, container)
}

get_type_violation(field, container) {
  field == "runAsUser"
  params := input.parameters[field]
  get_user_violation(params, container)
}

get_type_violation(field, container) {
  field != "runAsUser"
  params := input.parameters[field]
  get_violation(field, params, container)
}

is_exempt(container) {
  exempt_images := object.get(object.get(input, "parameters", {}), "exemptImages", [])
  img := container.image
  exemption := exempt_images[_]
  _matches_exemption(img, exemption)
}

_matches_exemption(img, exemption) {
  not endswith(exemption, "*")
  exemption == img
}

_matches_exemption(img, exemption) {
  endswith(exemption, "*")
  prefix := trim_suffix(exemption, "*")
  startswith(img, prefix)
}

get_user_violation(params, container) {
  rule := params.rule
  provided_user := get_field_value("runAsUser", container, input.review)
  not accept_users(rule, provided_user)
}

get_user_violation(params, container) {
  not get_field_value("runAsUser", container, input.review)
  params.rule = "MustRunAs"
}

get_user_violation(params, container) {
  params.rule = "MustRunAsNonRoot"
  not get_field_value("runAsUser", container, input.review)
  not get_field_value("runAsNonRoot", container, input.review)
}

accept_users("RunAsAny", provided_user) {true}

accept_users("MustRunAsNonRoot", provided_user) = res {res := provided_user != 0}

accept_users("MustRunAs", provided_user) = res  {
  ranges := input.parameters.runAsUser.ranges
  res := is_in_range(provided_user, ranges)
}

get_violation(field, params, container) {
  rule := params.rule
  provided_value := get_field_value(field, container, input.review)
  not is_array(provided_value)
  not accept_value(rule, provided_value, params.ranges)
}

get_violation(field, params, container) {
  rule := params.rule
  array_value := get_field_value(field, container, input.review)
  is_array(array_value)
  provided_value := array_value[_]
  not accept_value(rule, provided_value, params.ranges)
}

get_violation(field, params, container) {
  not get_field_value(field, container, input.review)
  params.rule == "MustRunAs"
}

accept_value("RunAsAny", provided_value, ranges) {true}

accept_value("MayRunAs", provided_value, ranges) = res { res := is_in_range(provided_value, ranges)}

accept_value("MustRunAs", provided_value, ranges) = res { res := is_in_range(provided_value, ranges)}

get_field_value(field, container, review) = out {
  container_value := get_seccontext_field(field, container)
  out := container_value
}

get_field_value(field, container, review) = out {
  not has_seccontext_field(field, container)
  review.kind.kind == "Pod"
  pod_value := get_seccontext_field(field, review.object.spec)
  out := pod_value
}

is_in_range(val, ranges) = res {
  matching := {1 | val >= ranges[j].min; val <= ranges[j].max}
  res := count(matching) > 0
}

has_seccontext_field(field, obj) {
  get_seccontext_field(field, obj)
}

has_seccontext_field(field, obj) {
  get_seccontext_field(field, obj) == false
}

get_seccontext_field(field, obj) = out {
  out = obj.securityContext[field]
}

input_containers[c] {
  c := input.review.object.spec.containers[_]
}
input_containers[c] {
  c := input.review.object.spec.initContainers[_]
}
input_containers[c] {
  c := input.review.object.spec.ephemeralContainers[_]
}
