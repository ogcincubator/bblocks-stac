walk(
  if (type == "object") and has("themes") then
  ."http://www.w3.org/ns/dcat#theme" = (.themes | map(
      .scheme as $SCHEME
      | .concepts | map(
          if .url then .url else
              if $SCHEME then
              "\($SCHEME)/\(.id | sub(".*?::"; ""))"
              else empty end
          end | {"@id": .}
      )
      ) | flatten )
  end
)
